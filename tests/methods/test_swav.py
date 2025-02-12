import argparse

import pytorch_lightning as pl
import torch
from pytorch_lightning import Trainer
from solo.methods import SwAV

from .utils import DATA_KWARGS, gen_base_kwargs, gen_batch, prepare_dummy_dataloaders


def test_swav():
    method_kwargs = {
        "output_dim": 256,
        "proj_hidden_dim": 2048,
        "num_prototypes": 300,
        "sk_iters": 3,
        "sk_epsilon": 0.05,
        "temperature": 0.2,
        "queue_size": 65536,
        "epoch_queue_starts": 0,
        "freeze_prototypes_epochs": 1,
    }

    BASE_KWARGS = gen_base_kwargs(cifar=False)
    kwargs = {**BASE_KWARGS, **DATA_KWARGS, **method_kwargs}
    model = SwAV(**kwargs)
    model.on_train_start()

    batch, batch_idx = gen_batch(BASE_KWARGS["batch_size"], BASE_KWARGS["n_classes"], "imagenet100")
    loss = model.training_step(batch, batch_idx)

    assert loss != 0

    BASE_KWARGS = gen_base_kwargs(cifar=True)
    kwargs = {**BASE_KWARGS, **DATA_KWARGS, **method_kwargs}
    model = SwAV(**kwargs)
    model.on_train_start()

    batch, batch_idx = gen_batch(BASE_KWARGS["batch_size"], BASE_KWARGS["n_classes"], "cifar10")
    loss = model.training_step(batch, batch_idx)

    assert loss != 0

    # test arguments
    parser = argparse.ArgumentParser()
    parser = pl.Trainer.add_argparse_args(parser)
    assert model.add_model_specific_args(parser) is not None

    # test parameters
    assert model.learnable_params is not None

    out = model(batch[1][0])
    assert (
        "logits" in out
        and isinstance(out["logits"], torch.Tensor)
        and out["logits"].size() == (BASE_KWARGS["batch_size"], BASE_KWARGS["n_classes"])
    )
    assert (
        "feats" in out
        and isinstance(out["feats"], torch.Tensor)
        and out["feats"].size() == (BASE_KWARGS["batch_size"], model.features_size)
    )
    assert (
        "z" in out
        and isinstance(out["z"], torch.Tensor)
        and out["z"].size() == (BASE_KWARGS["batch_size"], method_kwargs["output_dim"])
    )
    assert (
        "p" in out
        and isinstance(out["p"], torch.Tensor)
        and out["p"].size() == (BASE_KWARGS["batch_size"], method_kwargs["num_prototypes"])
    )

    # normal training
    BASE_KWARGS = gen_base_kwargs(cifar=False, multicrop=False)
    kwargs = {**BASE_KWARGS, **DATA_KWARGS, **method_kwargs}
    model = SwAV(**kwargs)

    args = argparse.Namespace(**kwargs)
    trainer = Trainer.from_argparse_args(
        args,
        checkpoint_callback=False,
        limit_train_batches=2,
        limit_val_batches=2,
    )
    train_dl, val_dl = prepare_dummy_dataloaders(
        "imagenet100",
        n_crops=BASE_KWARGS["n_crops"],
        n_small_crops=0,
        n_classes=BASE_KWARGS["n_classes"],
        multicrop=False,
    )
    trainer.fit(model, train_dl, val_dl)
