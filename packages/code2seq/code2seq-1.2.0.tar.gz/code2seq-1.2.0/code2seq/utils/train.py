from os.path import join

import torch
from commode_utils.callback import PrintEpochResultCallback, ModelCheckpointWithUpload
from omegaconf import DictConfig, OmegaConf
from pytorch_lightning import seed_everything, Trainer, LightningModule, LightningDataModule
from pytorch_lightning.callbacks import EarlyStopping, LearningRateMonitor, RichProgressBar
from pytorch_lightning.loggers import WandbLogger


def train(model: LightningModule, data_module: LightningDataModule, config: DictConfig):
    seed_everything(config.seed)
    params = config.train

    # define logger
    wandb_logger = WandbLogger(
        project=config.wandb.project,
        group=config.wandb.group,
        log_model=False,
        offline=config.wandb.offline,
        config=OmegaConf.to_container(config),
    )

    # define model checkpoint callback
    checkpoint_callback = ModelCheckpointWithUpload(
        dirpath=join(wandb_logger.experiment.dir, "checkpoints"),
        filename="{epoch:02d}-val_loss={val/loss:.4f}",
        monitor="val/loss",
        every_n_epochs=params.save_every_epoch,
        save_top_k=-1,
        auto_insert_metric_name=False,
    )
    # define early stopping callback
    early_stopping_callback = EarlyStopping(patience=params.patience, monitor="val/loss", verbose=True, mode="min")
    # define callback for printing intermediate result
    print_epoch_result_callback = PrintEpochResultCallback(after_test=False)
    # use gpu if it exists
    gpu = 1 if torch.cuda.is_available() else None
    # define learning rate logger
    lr_logger = LearningRateMonitor("step")
    # define progress bar callback
    progress_bar = RichProgressBar(refresh_rate_per_second=config.progress_bar_refresh_rate)
    trainer = Trainer(
        max_epochs=params.n_epochs,
        gradient_clip_val=params.clip_norm,
        deterministic=True,
        check_val_every_n_epoch=params.val_every_epoch,
        log_every_n_steps=params.log_every_n_steps,
        logger=wandb_logger,
        gpus=gpu,
        callbacks=[lr_logger, early_stopping_callback, checkpoint_callback, print_epoch_result_callback, progress_bar],
        resume_from_checkpoint=config.get("checkpoint", None),
    )

    trainer.fit(model=model, datamodule=data_module)
    trainer.test(datamodule=data_module, ckpt_path="best")
