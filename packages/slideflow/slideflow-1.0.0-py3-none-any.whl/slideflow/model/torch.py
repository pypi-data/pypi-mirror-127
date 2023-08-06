import os
import types
import time
import torch
import inspect
import torchvision
import pretrainedmodels
import slideflow as sf
import numpy as np

from os.path import join
from slideflow.util import log
from slideflow.model import base as _base
from slideflow.model.base import FeatureError
from slideflow.model import torch_utils
from slideflow.model.base import log_manifest
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter

class LinearBlock(torch.nn.Module):
    def __init__(self, in_ftrs, out_ftrs):
        super().__init__()
        self.in_ftrs = in_ftrs
        self.out_ftrs = out_ftrs

        self.linear = torch.nn.Linear(in_ftrs, out_ftrs)
        self.relu = torch.nn.ReLU(inplace=True)
        self.bn = torch.nn.BatchNorm1d(out_ftrs)

    def forward(self, x):
        x = self.linear(x)
        x = self.relu(x)
        x = self.bn(x)
        return x

class ModelWrapper(torch.nn.Module):
    def __init__(self, model, n_classes, num_slide_features=0, hidden_layers=None, drop_images=False):
        super().__init__()
        self.model = model
        self.n_classes = len(n_classes)
        self.drop_images = drop_images
        self.num_slide_features = num_slide_features
        self.num_hidden_layers = 0 if not hidden_layers else len(hidden_layers)

        if not drop_images:
            # Get the last linear layer prior to the logits layer
            if model.__class__.__name__ == 'Xception':
                num_ftrs = self.model.last_linear.in_features
                self.model.last_linear = torch.nn.Identity()
            elif model.__class__.__name__ == 'VGG':
                last_linear_name, last_linear = list(self.model.classifier.named_children())[-1]
                num_ftrs = last_linear.in_features
                setattr(self.model.classifier, last_linear_name, torch.nn.Identity())
            elif hasattr(self.model, 'fc'):
                num_ftrs = self.model.fc.in_features
                self.model.fc = torch.nn.Identity()
            elif hasattr(self.model, 'out_features'):
                num_ftrs = self.model.out_features
            else:
                raise _base.ModelError("Unable to find last linear layer")
        else:
            num_ftrs = 0

        # Add slide-level features
        num_ftrs += num_slide_features

        # Add hidden layers
        if hidden_layers:
            hl_ftrs = [num_ftrs] + hidden_layers
            for i in range(len(hidden_layers)):
                setattr(self, f'h{i}', LinearBlock(hl_ftrs[i], hl_ftrs[i+1]))
            num_ftrs = hidden_layers[-1]

        # Add the outcome/logits layers for each outcome, if multiple outcomes
        for i, n in enumerate(n_classes):
            setattr(self, f'fc{i}', torch.nn.Linear(num_ftrs, n))

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            if name == 'model':
                raise AttributeError()
            return getattr(self.model, name)

    def forward(self, img, slide_features=None):
        if slide_features is None and self.num_slide_features:
            raise ValueError(f"Expected 2 inputs, got 1")

        # Last linear of core convolutional model
        if not self.drop_images:
            x = self.model(img)

        # Merging image data with any slide-level input data
        if self.num_slide_features and not self.drop_images:
            x = torch.cat([x, slide_features], dim=1)
        elif self.num_slide_features:
            x = slide_features

        # Hidden layers
        if self.num_hidden_layers:
            x = self.h0(x)
        if self.num_hidden_layers > 1:
            for h in range(1, self.num_hidden_layers):
                x = getattr(self, f'h{h}')(x)

        # Return a list of outputs if we have multiple outcomes
        if self.n_classes > 1:
            out = [getattr(self, f'fc{i}')(x) for i in range(self.n_classes)]

        # Otherwise, return the single output
        else:
            out = self.fc0(x)

        return out

class ModelParams(_base._ModelParams):
    """Build a set of hyperparameters."""

    def __init__(self, model='xception', loss='CrossEntropy', **kwargs):
        self.OptDict = {
            'Adadelta': torch.optim.Adadelta,
            'Adagrad': torch.optim.Adagrad,
            'Adam': torch.optim.Adam,
            'AdamW': torch.optim.AdamW,
            'SparseAdam': torch.optim.SparseAdam,
            'Adamax': torch.optim.Adamax,
            'ASGD': torch.optim.ASGD,
            'LBFGS': torch.optim.LBFGS,
            'RMSprop': torch.optim.RMSprop,
            'Rprop': torch.optim.Rprop,
            'SGD': torch.optim.SGD
        }
        self.ModelDict = {
            'resnet18': torchvision.models.resnet18,
            'resnet50': torchvision.models.resnet50,
            'alexnet': torchvision.models.alexnet,
            'squeezenet': torchvision.models.squeezenet.squeezenet1_1,
            'densenet': torchvision.models.densenet161,
            'inception': torchvision.models.inception_v3,
            'googlenet': torchvision.models.googlenet,
            'shufflenet': torchvision.models.shufflenet_v2_x1_0,
            'resnext50_32x4d': torchvision.models.resnext50_32x4d,
            'vgg16': torchvision.models.vgg16, # needs support added
            'mobilenet_v2': torchvision.models.mobilenet_v2,
            'mobilenet_v3_small': torchvision.models.mobilenet_v3_small,
            'mobilenet_v3_large': torchvision.models.mobilenet_v3_large,
            'wide_resnet50_2': torchvision.models.wide_resnet50_2,
            'mnasnet': torchvision.models.mnasnet1_0,
            'xception': pretrainedmodels.xception
        }
        self.LinearLossDict = {
            'L1': torch.nn.L1Loss,
            'MSE': torch.nn.MSELoss,
            'NLL': torch.nn.NLLLoss, #negative log likelihood
            'HingeEmbedding': torch.nn.HingeEmbeddingLoss,
            'SmoothL1': torch.nn.SmoothL1Loss,
            'CosineEmbedding': torch.nn.CosineEmbeddingLoss,
        }
        self.AllLossDict = {
            'CrossEntropy': torch.nn.CrossEntropyLoss,
            'CTC': torch.nn.CTCLoss,
            'PoissonNLL': torch.nn.PoissonNLLLoss,
            'GaussianNLL': torch.nn.GaussianNLLLoss,
            'KLDiv': torch.nn.KLDivLoss,
            'BCE': torch.nn.BCELoss,
            'BCEWithLogits': torch.nn.BCEWithLogitsLoss,
            'MarginRanking': torch.nn.MarginRankingLoss,
            'MultiLabelMargin': torch.nn.MultiLabelMarginLoss,
            'Huber': torch.nn.HuberLoss,
            'SoftMargin': torch.nn.SoftMarginLoss,
            'MultiLabelSoftMargin': torch.nn.MultiLabelSoftMarginLoss,
            'MultiMargin': torch.nn.MultiMarginLoss,
            'TripletMargin': torch.nn.TripletMarginLoss,
            'TripletMarginWithDistance': torch.nn.TripletMarginWithDistanceLoss,
            'L1': torch.nn.L1Loss,
            'MSE': torch.nn.MSELoss,
            'NLL': torch.nn.NLLLoss, #negative log likelihood
            'HingeEmbedding': torch.nn.HingeEmbeddingLoss,
            'SmoothL1': torch.nn.SmoothL1Loss,
            'CosineEmbedding': torch.nn.CosineEmbeddingLoss,
        }
        super().__init__(model=model, loss=loss, **kwargs)
        assert self.model in self.ModelDict.keys()
        assert self.optimizer in self.OptDict.keys()
        assert self.loss in self.AllLossDict
        if not self.include_top:
            raise _base.HyperParameterError("PyTorch backend does not currently support include_top=False.")

    def get_opt(self, params_to_update):
        return self.OptDict[self.optimizer](params_to_update, lr=self.learning_rate)

    def get_loss(self):
        return self.AllLossDict[self.loss]()

    def build_model(self, labels=None, num_classes=None, num_slide_features=0, pretrain=None, checkpoint=None):
        assert num_classes is not None or labels is not None
        if num_classes is None:
            num_classes = self._detect_classes_from_labels(labels)
        if not isinstance(num_classes, dict):
            num_classes = {'out-0': num_classes}

        # Build base model
        if self.model in ('xception',):
            _model = self.ModelDict[self.model](num_classes=1000, pretrained=pretrain)
        else:
            model_fn = self.ModelDict[self.model]
            # Only pass kwargs accepted by model function
            model_fn_sig = inspect.signature(model_fn)
            model_kw = [param.name for param in model_fn_sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD]
            model_kwargs = {'image_size': self.tile_px} if 'image_size' in model_kw else {}
            _model = model_fn(pretrained=pretrain, **model_kwargs)

        # Add final layers to models
        hidden_layers = [self.hidden_layer_width for h in range(self.hidden_layers)]
        _model = ModelWrapper(_model, num_classes.values(), num_slide_features, hidden_layers, self.drop_images)

        return _model

    def model_type(self):
        if self.loss == 'NLL':
            return 'cph'
        elif self.loss in self.LinearLossDict:
            return 'linear'
        else:
            return 'categorical'

class Trainer:
    def __init__(self, hp, outdir, labels, patients, name=None, manifest=None, slide_input=None, feature_sizes=None,
                 feature_names=None, outcome_names=None, mixed_precision=True,
                 config=None, use_neptune=None, neptune_api=None, neptune_workspace=None):

        self.hp = hp
        self.outdir = outdir
        self.labels = labels
        self.patients = patients
        self.name = name
        self.manifest = manifest
        self.model = None
        self.mixed_precision = mixed_precision

        # Slide-level input args
        self.slide_input = None if not slide_input else {k:[float(vi) for vi in v] for k,v in slide_input.items()}
        self.feature_names = feature_names
        self.feature_sizes = feature_sizes
        self.num_slide_features = 0 if not feature_sizes else sum(feature_sizes)

        self.normalizer = self.hp.get_normalizer()
        if self.normalizer: log.info(f'Using realtime {self.hp.normalizer} normalization')
        self.outcome_names = outcome_names
        outcome_labels = np.array(list(labels.values()))
        if len(outcome_labels.shape) == 1:
            outcome_labels = np.expand_dims(outcome_labels, axis=1)
        if not self.outcome_names:
            self.outcome_names = [f'Outcome {i}' for i in range(outcome_labels.shape[1])]
        if not len(self.outcome_names) == outcome_labels.shape[1]:
            raise sf.util.UserError(f"Number of provided outcome names ({len(self.outcome_names)}) does not match " + \
                                    f"the number of outcomes ({outcome_labels.shape[1]})")
        if not os.path.exists(outdir): os.makedirs(outdir)

    @property
    def num_outcomes(self):
        if self.hp.model_type() == 'categorical':
            return len(self.outcome_names)
        else:
            return 1

    def load(self, model):
        self.model = self.hp.build_model(labels=self.labels, num_slide_features=self.num_slide_features)
        self.model.load_state_dict(torch.load(model))

    def evaluate(self, dataset, batch_size=None, histogram=False, save_predictions=False, permutation_importance=False):

        # Load and initialize model
        if permutation_importance:
            raise NotImplementedError("permutation_importance not yet implemented for PyTorch backend.")
        if not self.model:
            raise sf.util.UserError("Model has not been loaded, unable to evaluate.")
        device = torch.device('cuda:0')
        self.model.to(device)
        self.model.eval()
        loss_fn = self.hp.get_loss()
        log_manifest(None, dataset.tfrecords(), self.labels, join(self.outdir, 'slide_manifest.csv'))
        if not batch_size: batch_size = self.hp.batch_size

        # Setup dataloaders
        interleave_args = types.SimpleNamespace(
            rank=0,
            num_replicas=1,
            labels=self.labels,
            chunk_size=16,
            normalizer=self.normalizer,
            pin_memory=True,
            num_workers=8,
            onehot=False,
        )

        torch_dataset = dataset.torch(infinite=False, batch_size=batch_size, augment=False, incl_slidenames=True, **vars(interleave_args))

        metric_kwargs = types.SimpleNamespace(
            dataset=torch_dataset,
            model=self.model,
            model_type=self.hp.model_type(),
            labels=self.labels,
            patients=self.patients,
            outcome_names=self.outcome_names,
            data_dir=self.outdir,
            num_tiles=dataset.num_tiles,
            label='eval'
        )

        # Preparations for calculating accuracy/loss in metrics_from_dataset()
        def update_corrects(pred, labels, running_corrects):
            labels = self.labels_to_device(labels, device)
            return self.update_corrects(pred, labels, running_corrects)

        def update_loss(pred, labels, running_loss, size):
            labels = self.labels_to_device(labels, device)
            loss = self.calculate_loss(pred, labels, loss_fn)
            return running_loss + (loss.item() * size)

        pred_args = types.SimpleNamespace(
            multi_outcome=(self.num_outcomes > 1),
            update_corrects=update_corrects,
            update_loss=update_loss,
            running_corrects=(0 if not (self.num_outcomes > 1) else {f'out-{o}':0 for o in range(self.num_outcomes)}),
            num_slide_features=self.num_slide_features,
            slide_input=self.slide_input
        )

        # Generate performance metrics
        log.info('Calculating performance metrics...')
        metrics, acc, loss = sf.statistics.metrics_from_dataset(histogram=histogram,
                                                                verbose=True,
                                                                save_predictions=save_predictions,
                                                                pred_args=pred_args,
                                                                **vars(metric_kwargs))
        results_dict = { 'eval': {'loss': loss} }
        if self.hp.model_type() == 'categorical':
            results_dict['eval'].update({'accuracy': acc})
        for metric in metrics:
            if metrics[metric]:
                log.info(f"Tile {metric}: {metrics[metric]['tile']}")
                log.info(f"Slide {metric}: {metrics[metric]['slide']}")
                log.info(f"Patient {metric}: {metrics[metric]['patient']}")
                results_dict['eval'].update({
                    f'tile_{metric}': metrics[metric]['tile'],
                    f'slide_{metric}': metrics[metric]['slide'],
                    f'patient_{metric}': metrics[metric]['patient']
                })

        results_log = os.path.join(self.outdir, 'results_log.csv')
        sf.util.update_results_log(results_log, 'eval_model', results_dict)
        return results_dict

    def labels_to_device(self, labels, device):
        '''Moves a set of outcome labels to the given device.'''

        if self.num_outcomes > 1:
            labels = {k: l.to(device, non_blocking=True) for k,l in labels.items()}
        elif isinstance(labels, dict):
            return torch.stack(list(labels.values()), dim=1).to(device, non_blocking=True)
        else:
            labels = labels.to(device, non_blocking=True)
        return labels

    def calculate_loss(self, outputs, labels, loss_fn):
        '''Calculates loss in a manner compatible with multiple outcomes.'''

        if self.num_outcomes > 1:
            loss = sum([loss_fn(out, labels[f'out-{o}']) for o, out in enumerate(outputs)])
        else:
            loss = loss_fn(outputs, labels)
        return loss

    def accuracy_description(self, running_corrects, num_records=1):
        '''Reports accuracy of each outcome.'''

        if self.hp.model_type() == 'categorical':
            if self.num_outcomes > 1:
                acc_desc = ''
                acc_list = [running_corrects[r] / num_records for r in running_corrects]
                for o in range(len(running_corrects)):
                    acc_desc += f"out-{o} acc: {running_corrects[f'out-{o}'] / num_records:.4f} "
                return acc_desc, acc_list
            else:
                return f'acc: {running_corrects / num_records:.4f}', running_corrects / num_records
        else:
            return '', running_corrects

    def update_corrects(self, outputs, labels, running_corrects):
        '''Updates running accuracy in a manner compatible with multiple outcomes.'''

        if self.hp.model_type() == 'categorical':
            if self.num_outcomes > 1:
                for o, out in enumerate(outputs):
                    _, preds = torch.max(out, 1)
                    running_corrects[f'out-{o}'] += torch.sum(preds == labels[f'out-{o}'].data)
            else:
                _, preds = torch.max(outputs, 1)
                running_corrects += torch.sum(preds == labels.data)
            return running_corrects
        else:
            return 0

    def log_epoch(self, phase, epoch, loss, accuracy_description, starttime):
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - starttime))
        log.info(f'{sf.util.bold(sf.util.blue(phase))} Epoch {epoch} | loss: {loss:.4f} {accuracy_description} (Elapsed: {elapsed})')

    def train(self, train_dts, val_dts, validate_on_batch=512, validation_batch_size=32, validation_steps=50,
              save_predictions=False, skip_metrics=False, seed=0, log_frequency=20, starting_epoch=0,
              ema_observations=20, ema_smoothing=2, use_tensorboard=True, steps_per_epoch_override=0,
              multi_gpu=True, pretrain='imagenet', checkpoint=None, resume_training=None):

        if resume_training is not None:
            raise NotImplementedError("PyTorch backend does not support `resume_training`; please use `checkpoint`")

        starting_epoch = max(starting_epoch, 1)
        results = {'epochs': {}}
        device = torch.device('cuda:0')
        global_step = 0
        early_stop = False
        last_ema, ema_one_check_prior, ema_two_checks_prior = -1, -1, -1
        moving_average = []

        if (self.hp.early_stop and self.hp.early_stop_method == 'accuracy' and
           self.hp.model_type() == 'categorical' and self.num_outcomes > 1):

           raise sf.util.UserError("Cannot combine 'accuracy' early stopping with multiple categorical outcomes.")

        # Enable TF32 (should be enabled by default)
        torch.backends.cuda.matmul.allow_tf32 = True  # Allow PyTorch to internally use tf32 for matmul
        torch.backends.cudnn.allow_tf32 = True        # Allow PyTorch to internally use tf32 for convolutions

        # Training preparation
        val_tfr = val_dts.tfrecords() if val_dts else None
        log_manifest(train_dts.tfrecords(), val_tfr, self.labels, join(self.outdir, 'slide_manifest.csv'))
        if steps_per_epoch_override:
            steps_per_epoch = steps_per_epoch_override
            log.info(f"Overriding steps per epoch = {steps_per_epoch_override}")
        else:
            steps_per_epoch = train_dts.num_tiles // self.hp.batch_size
            log.info(f"Steps per epoch = {steps_per_epoch}")
        multi_outcome = (self.num_outcomes > 1)
        if use_tensorboard:
            writer = SummaryWriter(self.outdir, flush_secs=60)

        # Build model
        if checkpoint:
            log.info(f"Loading checkpoint at {sf.util.green(checkpoint)}")
            self.load(checkpoint)
        else:
            self.model = self.hp.build_model(labels=self.labels, pretrain=pretrain, num_slide_features=self.num_slide_features)

        # Print model summary
        empty_inp = [torch.empty([self.hp.batch_size, 3, train_dts.tile_px, train_dts.tile_px])]
        if self.num_slide_features:
            empty_inp += [torch.empty([self.hp.batch_size, self.num_slide_features])]
        if log.getEffectiveLevel() <= 20:
            torch_utils.print_module_summary(self.model, empty_inp)

        # Multi-GPU
        inference_model = self.model
        if multi_gpu:
            self.model = torch.nn.DataParallel(self.model)

        self.model = self.model.to(device)

        # Setup dataloaders
        interleave_args = types.SimpleNamespace(
            rank=0,
            num_replicas=1,
            labels=self.labels,
            chunk_size=8,
            normalizer=self.normalizer,
            pin_memory=True,
            num_workers=4,
            onehot=False,
            incl_slidenames=True
        )

        dataloaders = {
            'train': iter(train_dts.torch(infinite=True, batch_size=self.hp.batch_size, augment=True, **vars(interleave_args)))
        }
        if val_dts is not None:
            dataloaders['val'] = val_dts.torch(infinite=False, batch_size=validation_batch_size, augment=False, **vars(interleave_args))
            mid_train_val_dts = torch_utils.cycle(dataloaders['val'])
            val_log_msg = '' if not validate_on_batch else f'every {str(validate_on_batch)} steps and '
            log.debug(f'Validation during training: {val_log_msg}at epoch end')
            if validation_steps:
                num_samples = validation_steps * self.hp.batch_size
                log.debug(f'Using {validation_steps} batches ({num_samples} samples) each validation check')
            else:
                log.debug(f'Using entire validation set each validation check')
        else:
            mid_train_val_dts = None
            log.debug('Validation during training: None')

        # Model parameters and loss
        params_to_update = self.model.parameters()
        optimizer = self.hp.get_opt(params_to_update)
        loss_fn = self.hp.get_loss()
        if self.mixed_precision:
            scaler = torch.cuda.amp.GradScaler()

        # Epoch loop
        for epoch in range(starting_epoch, max(self.hp.epochs)+1):
            np.random.seed(seed+epoch)
            if early_stop: break
            if log.getEffectiveLevel() <= 20: print()
            log.info(sf.util.bold('Epoch ' + str(epoch) + '/' + str(max(self.hp.epochs))))

            for phase in dataloaders:
                num_records = 0
                running_loss = 0.0
                step = 1
                starttime = time.time()

                if multi_outcome:   running_corrects = {f'out-{o}':0 for o in range(self.num_outcomes)}
                else:               running_corrects = 0

                if phase == 'train':
                    self.model.train()

                    # Setup up mid-training validation
                    # === Loop through training dataset ===============================================================
                    pb = tqdm(total=(steps_per_epoch * self.hp.batch_size), unit='img', leave=False)
                    while step < steps_per_epoch:
                        images, labels, slides = next(dataloaders['train'])
                        images = images.to(device, non_blocking=True)
                        labels = self.labels_to_device(labels, device)

                        # Training step
                        optimizer.zero_grad()
                        with torch.set_grad_enabled(True):
                            with torch.cuda.amp.autocast() if self.mixed_precision else sf.model.no_scope():
                                # Slide-level features
                                if self.num_slide_features:
                                    inp = (images, torch.tensor([self.slide_input[s] for s in slides]).to(device))
                                else:
                                    inp = (images,)
                                outputs = self.model(*inp)
                                loss = self.calculate_loss(outputs, labels, loss_fn)

                            # Update weights
                            if self.mixed_precision:
                                scaler.scale(loss).backward()
                                scaler.step(optimizer)
                                scaler.update()
                            else:
                                loss.backward()
                                optimizer.step()

                        # Record accuracy and loss
                        num_records += images.size(0)
                        running_corrects = self.update_corrects(outputs, labels, running_corrects)
                        acc_desc, _ = self.accuracy_description(running_corrects, num_records)
                        running_loss += loss.item() * images.size(0)
                        pb.set_description(f'{sf.util.bold(sf.util.blue(phase))} loss: {running_loss / num_records:.4f} {acc_desc}')
                        pb.update(images.size(0))

                        # Log to tensorboard
                        if use_tensorboard and global_step % log_frequency == 0:
                            writer.add_scalar('Loss/train', loss.item(), global_step)
                            if self.hp.model_type() == 'categorical':
                                if self.num_outcomes > 1:
                                    for o, out in enumerate(outputs):
                                        writer.add_scalar(f'Accuracy-{o}/train', running_corrects[f'out-{o}'] / num_records, global_step)
                                else:
                                    writer.add_scalar('Accuracy/train', running_corrects / num_records, global_step)

                        # === Mid-training validation =================================================================
                        if val_dts and validate_on_batch and (step % validate_on_batch == 0) and step > 0:
                            self.model.eval()
                            running_val_loss = 0
                            num_val = 0

                            if multi_outcome:   running_val_correct = {f'out-{o}':0 for o in range(self.num_outcomes)}
                            else:               running_val_correct = 0

                            for _ in range(validation_steps):
                                val_img, val_label, slides = next(mid_train_val_dts)
                                val_img = val_img.to(device)

                                with torch.no_grad():
                                    with torch.cuda.amp.autocast() if self.mixed_precision else sf.model.no_scope():
                                        if self.num_slide_features:
                                            inp = (val_img, torch.tensor([self.slide_input[s] for s in slides]).to(device))
                                        else:
                                            inp = (val_img,)
                                        val_outputs = inference_model(*inp)
                                        val_label = self.labels_to_device(val_label, device)
                                        val_loss = self.calculate_loss(val_outputs, val_label, loss_fn)

                                running_val_loss += val_loss.item() * val_img.size(0)
                                running_val_correct = self.update_corrects(val_outputs, val_label, running_val_correct)
                                num_val += val_img.size(0)
                            val_loss = running_val_loss / num_val
                            val_acc_desc, val_acc = self.accuracy_description(running_val_correct, num_val)

                            log_msg = f'Batch {step}: val loss: {val_loss:.4f}{val_acc_desc}'

                            # EMA & early stopping --------------------------------------------------------------------
                            early_stop_val = val_acc if self.hp.early_stop_method == 'accuracy' else val_loss
                            moving_average += [early_stop_val]
                            if len(moving_average) >= ema_observations:
                                moving_average.pop(0) # Only keep track of the last [ema_observations]
                                if last_ema == -1:
                                    last_ema = sum(moving_average) / len(moving_average) # Simple moving average
                                    log_msg += f' (SMA: {last_ema:.3f})'
                                else:
                                    last_ema = (early_stop_val * (ema_smoothing / (1 + ema_observations))) + \
                                               (last_ema * (1 - (ema_smoothing / (1 + ema_observations))))
                                    log_msg += f' (EMA: {last_ema:.3f})'

                                if self.hp.early_stop and ema_two_checks_prior != -1 and epoch > self.hp.early_stop_patience:
                                    if ((self.hp.early_stop_method == 'accuracy' and last_ema <= ema_two_checks_prior) or
                                        (self.hp.early_stop_method == 'loss'     and last_ema >= ema_two_checks_prior)):

                                        log.info(f'Early stop triggered: epoch {epoch}, step {step}')
                                        if epoch not in self.hp.epochs:
                                            self.hp.epochs += [epoch]
                                            early_stop = True
                                            break

                                ema_two_checks_prior = ema_one_check_prior
                                ema_one_check_prior = last_ema
                            # -----------------------------------------------------------------------------------------
                            log.info(log_msg)
                            if use_tensorboard:
                                writer.add_scalar('Loss/test', val_loss, global_step)
                                if self.hp.model_type() == 'categorical':
                                    if self.num_outcomes > 1:
                                        for o, out in enumerate(outputs):
                                            writer.add_scalar(f'Accuracy-{o}/test', running_val_correct[f'out-{o}'] / num_val, global_step)
                                    else:
                                        writer.add_scalar('Accuracy/test', running_val_correct / num_val, global_step)

                            self.model.train()
                        # =============================================================================================

                        step += 1
                        global_step += 1

                    pb.close()
                    # === [end training loop] =========================================================================

                    # Calculate epoch-level accuracy and loss
                    epoch_loss = running_loss / num_records
                    epoch_acc_desc, epoch_accuracy = self.accuracy_description(running_corrects, num_records)
                    self.log_epoch('train', epoch, epoch_loss, epoch_acc_desc, starttime)

                    if f'epoch{epoch}' not in results['epochs']:
                        results['epochs'][f'epoch{epoch}'] = {}
                    epoch_metrics = {'loss': epoch_loss}
                    if self.hp.model_type() == 'categorical':
                        if isinstance(epoch_accuracy, (float, int)):
                            epoch_metrics.update({'accuracy': epoch_accuracy})
                        elif isinstance(epoch_accuracy, (list)):
                            epoch_metrics.update({'accuracy': [e.cpu().numpy().tolist() for e in epoch_accuracy]})
                        else:
                            epoch_metrics.update({'accuracy': epoch_accuracy.cpu().numpy().tolist()})
                    results['epochs'][f'epoch{epoch}'].update({f'train_metrics': epoch_metrics})

                # === Full dataset validation =========================================================================
                # Perform full evaluation if the epoch is one of the predetermined epochs at which to save/eval a model
                if phase == 'val' and (val_dts is not None) and epoch in self.hp.epochs:
                    optimizer.zero_grad()
                    self.model.eval()
                    model_name = self.name if self.name else 'trained_model'
                    results_log = os.path.join(self.outdir, 'results_log.csv')
                    save_path = os.path.join(self.outdir, f'{model_name}_epoch{epoch}')
                    torch.save(self.model.state_dict(), save_path)
                    log.info(f"Model saved to {sf.util.green(save_path)}")

                    epoch_results = {}
                    if not skip_metrics:
                        # Preparations for calculating accuracy/loss in metrics_from_dataset()
                        def update_corrects(pred, labels, running_corrects):
                            labels = self.labels_to_device(labels, device)
                            return self.update_corrects(pred, labels, running_corrects)

                        def update_loss(pred, labels, running_loss, size):
                            labels = self.labels_to_device(labels, device)
                            loss = self.calculate_loss(pred, labels, loss_fn)
                            return running_loss + (loss.item() * size)

                        pred_args = types.SimpleNamespace(
                            multi_outcome=(self.num_outcomes > 1),
                            update_corrects=update_corrects,
                            update_loss=update_loss,
                            running_corrects=(0 if not multi_outcome else {f'out-{o}':0 for o in range(self.num_outcomes)}),
                            num_slide_features=self.num_slide_features,
                            slide_input=self.slide_input
                        )

                        # Calculate patient/slide/tile - level metrics (AUC, R-squared, C-index, etc)
                        metrics, acc, loss = sf.statistics.metrics_from_dataset(inference_model,
                                                                                model_type=self.hp.model_type(),
                                                                                labels=self.labels,
                                                                                patients=self.patients,
                                                                                dataset=dataloaders['val'],
                                                                                data_dir=self.outdir,
                                                                                outcome_names=self.outcome_names,
                                                                                save_predictions=save_predictions,
                                                                                pred_args=pred_args)

                        epoch_metrics = {'loss': epoch_loss}
                        if self.hp.model_type() == 'categorical':
                            epoch_metrics.update({'accuracy': acc})
                        results['epochs'][f'epoch{epoch}'].update({f'val_metrics': epoch_metrics})

                        self.log_epoch('val', epoch, loss, self.accuracy_description(acc)[0], starttime)

                        for metric in metrics:
                            if metrics[metric]['tile'] is None: continue
                            epoch_results['tile'] = metrics[metric]['tile']
                            epoch_results['slide'] = metrics[metric]['slide']
                            epoch_results['patient'] = metrics[metric]['patient']
                    results['epochs'][f'epoch{epoch}'].update(epoch_results)
                    sf.util.update_results_log(results_log, 'trained_model', {f'epoch{epoch}': results['epochs'][f'epoch{epoch}']})
                # =====================================================================================================

        return results

class LinearTrainer(Trainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CPHTrainer(Trainer):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

class Features:
    """Interface for obtaining logits and features from intermediate layer activations from Slideflow models.

    Use by calling on either a batch of images (returning outputs for a single batch), or by calling on a
    :class:`slideflow.WSI` object, which will generate an array of spatially-mapped activations matching
    the slide.

    Examples
        *Calling on batch of images:*

        .. code-block:: python

            interface = Features('/model/path', layers='postconv')
            for image_batch in train_data:
                # Return shape: (batch_size, num_features)
                batch_features = interface(image_batch)

        *Calling on a slide:*

        .. code-block:: python

            slide = sf.slide.WSI(...)
            interface = Features('/model/path', layers='postconv')
            # Return shape: (slide.grid.shape[0], slide.grid.shape[1], num_features):
            activations_grid = interface(slide)

    Note:
        When this interface is called on a batch of images, no image processing or stain normalization will be
        performed, as it is assumed that normalization will occur during data loader image processing.
        When the interface is called on a `slideflow.WSI`, the normalization strategy will be read from the model
        configuration file, and normalization will be performed on image tiles extracted from the WSI. If this interface
        was created from an existing model and there is no model configuration file to read, a
        slideflow.slide.StainNormalizer object may be passed during initialization via the argument `wsi_normalizer`.

    """

    def __init__(self, path, layers='postconv', include_logits=False, mixed_precision=True, device=None):
        """Creates an activations interface from a saved slideflow model which outputs feature activations
        at the designated layers.

        Intermediate layers are returned in the order of layers. Logits are returned last.

        Args:
            path (str): Path to saved Slideflow model.
            layers (list(str), optional): Layers from which to generate activations.  The post-convolution activation layer
                is accessed via 'postconv'. Defaults to 'postconv'.
            include_logits (bool, optional): Include logits in output. Will be returned last. Defaults to False.
            mixed_precision (bool, optional): Use mixed precision. Defaults to True.
            device (:class:`torch.device`, optional): Device for model. Defaults to torch.device('cuda')
        """

        if layers and isinstance(layers, str): layers = [layers]
        self.path = path
        self.num_logits = 0
        self.num_features = 0
        self.mixed_precision = mixed_precision
        self.activation = {}
        self.layers = layers
        self.include_logits = include_logits
        self.device = device if device is not None else torch.device('cuda')

        if path is not None:
            try:
                config = sf.util.get_model_config(path)
            except:
                raise FeatureError(f"Unable to find configuration for model {path}")

            self.hp = ModelParams()
            self.hp.load_dict(config['hp'])
            self.wsi_normalizer = self.hp.get_normalizer()
            self.tile_px = self.hp.tile_px
            self._model = self.hp.build_model(num_classes=len(config['outcome_labels'])) #labels=
            self._model.load_state_dict(torch.load(path))
            self._model.to(self.device)
            if self._model.__class__.__name__ == 'ModelWrapper':
                self.model_type = self._model.model.__class__.__name__
            else:
                self.model_type = self._model.__class__.__name__
            self._build()
            self._model.eval()

    @classmethod
    def from_model(cls, model, tile_px, layers='postconv', include_logits=False, mixed_precision=True,
                   wsi_normalizer=None, device=None):
        """Creates an activations interface from a loaded slideflow model which outputs feature activations
        at the designated layers.

        Intermediate layers are returned in the order of layers. Logits are returned last.

        Args:
            model (:class:`tensorflow.keras.models.Model`): Loaded model.
            tile_px (int): Width/height of input image size.
            layers (list(str), optional): Layers from which to generate activations.  The post-convolution activation layer
                is accessed via 'postconv'. Defaults to 'postconv'.
            include_logits (bool, optional): Include logits in output. Will be returned last. Defaults to False.
            wsi_normalizer (:class:`slideflow.slide.StainNormalizer`): Stain normalizer to use on whole-slide images.
                Is not used on individual tile datasets via __call__. Defaults to None.
            device (:class:`torch.device`, optional): Device for model. Defaults to torch.device('cuda')
        """

        obj = cls(None, layers, include_logits, mixed_precision, device)
        if isinstance(model, torch.nn.Module):
            obj._model = model.to(obj.device)
            obj._model.eval()
        else:
            raise TypeError("Provided model is not a valid PyTorch model.")
        obj.hp = None
        if obj._model.__class__.__name__ == 'ModelWrapper':
            obj.model_type = obj._model.model.__class__.__name__
        else:
            obj.model_type = obj._model.__class__.__name__
        obj.tile_px = tile_px
        obj.wsi_normalizer = wsi_normalizer
        obj._build()
        return obj

    def __call__(self, inp, **kwargs):
        """Process a given input and return activations and/or logits. Expects either a batch of images or
        a :class:`slideflow.slide.WSI` object."""

        if isinstance(inp, sf.slide.WSI):
            return self._predict_slide(inp, **kwargs)
        else:
            return self._predict(inp)

    def _predict_slide(self, slide, batch_size=128, dtype=np.float16, **kwargs):
        """Generate activations from slide => activation grid array."""
        total_out = self.num_features + self.num_logits
        features_grid = np.zeros((slide.grid.shape[1], slide.grid.shape[0], total_out), dtype=dtype)
        generator = slide.build_generator(shuffle=False, include_loc='grid', show_progress=True, **kwargs)

        if not generator:
            log.error(f"No tiles extracted from slide {sf.util.green(slide.name)}")
            return

        class SlideIterator(torch.utils.data.IterableDataset):
            def __init__(self, parent, *args, **kwargs):
                super(SlideIterator).__init__(*args, **kwargs)
                self.parent = parent
            def __iter__(self):
                for image_dict in generator():
                    np_image = torch.from_numpy(image_dict['image'])
                    if self.parent.wsi_normalizer:
                        np_image = self.parent.wsi_normalizer.rgb_to_rgb(np_image)
                    np_image = np_image.permute(2, 0, 1) # WHC => CWH
                    loc = np.array(image_dict['loc'])
                    np_image = np_image / 127.5 - 1
                    yield np_image, loc

        tile_dataset = torch.utils.data.DataLoader(SlideIterator(self), batch_size=batch_size)

        act_arr = []
        loc_arr = []
        for i, (batch_images, batch_loc) in enumerate(tile_dataset):
            model_out = self._predict(batch_images)
            if not isinstance(model_out, list): model_out = [model_out]
            act_arr += [np.concatenate([m.cpu().detach().numpy() for m in model_out])]
            loc_arr += [batch_loc]

        act_arr = np.concatenate(act_arr)
        loc_arr = np.concatenate(loc_arr)

        for i, act in enumerate(act_arr):
            xi = loc_arr[i][0]
            yi = loc_arr[i][1]
            features_grid[yi][xi] = act

        return features_grid

    def _predict(self, inp):
        """Return activations for a single batch of images."""
        with torch.cuda.amp.autocast() if self.mixed_precision else sf.model.no_scope():
            with torch.no_grad():
                logits = self._model(inp.to(self.device))

        layer_activations = []
        if self.layers:
            for l in self.layers:
                act = self.activation[l]
                if l == 'postconv':
                    act = self._postconv_processing(act)
                layer_activations.append(act)

        if self.include_logits:
            layer_activations += [logits]
        self.activation = {}
        return layer_activations

    def _get_postconv(self):
        """Returns post-convolutional layer."""

        if self.model_type == 'ViT':
            return self._model.to_latent
        if self.model_type in ('ResNet', 'Inception3', 'GoogLeNet'):
            return self._model.avgpool
        if self.model_type in ('AlexNet', 'SqueezeNet', 'VGG', 'MobileNetV2', 'MobileNetV3', 'MNASNet'):
            return next(self._model.classifier.children())
        if self.model_type == 'DenseNet':
            return self._model.features.norm5
        if self.model_type == 'ShuffleNetV2':
            return list(self._model.conv5.children())[1]
        if self.model_type == 'Xception':
            return self._model.bn4
        raise FeatureError(f"'postconv' layer not configured for model type {self.model_type}")

    def _postconv_processing(self, output):
        """Applies processing (pooling, resizing) to post-convolutional outputs,
        to convert output to the shape (batch_size, num_features)"""

        def pool(x):
            return torch.nn.functional.adaptive_avg_pool2d(x, (1, 1))

        def squeeze(x):
            return x.view(x.size(0), -1)

        if self.model_type in ('ViT', 'AlexNet', 'VGG', 'MobileNetV2', 'MobileNetV3', 'MNASNet'):
            return output
        if self.model_type in ('ResNet', 'Inception3', 'GoogLeNet'):
            return squeeze(output)
        if self.model_type in ('SqueezeNet', 'DenseNet', 'ShuffleNetV2', 'Xception'):
            return squeeze(pool(output))
        return output

    def _build(self):
        """Builds the interface model that outputs feature activations at the designated layers and/or logits.
            Intermediate layers are returned in the order of layers. Logits are returned last."""

        self.activation = {}
        def get_activation(name):
            def hook(model, input, output):
                self.activation[name] = output.detach()
            return hook

        if isinstance(self.layers, list):
            for l in self.layers:
                if l == 'postconv':
                    self._get_postconv().register_forward_hook(get_activation('postconv'))
                else:
                    getattr(self._model, l).register_forward_hook(get_activation(l))
        elif self.layers is not None:
            raise TypeError(f"Unrecognized type {type(self.layers)} for self.layers")

        # Calculate output and layer sizes
        rand_data = torch.rand(1, 3, self.tile_px, self.tile_px)
        output = self._model(rand_data.to(self.device))
        self.num_logits = output.shape[1] if self.include_logits else 0
        self.num_features = sum([f.shape[1] for f in self.activation.values()])

        if self.include_logits:
            log.debug(f'Number of logits: {self.num_logits}')
        log.debug(f'Number of activation features: {self.num_features}')