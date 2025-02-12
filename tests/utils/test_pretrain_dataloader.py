import numpy as np
from PIL import Image
from torchvision.datasets.cifar import CIFAR10
from torch.utils.data import DataLoader
from solo.utils.pretrain_dataloader import (
    prepare_n_crop_transform,
    prepare_transform,
    prepare_multicrop_transform,
    prepare_dataloader,
    prepare_datasets,
)


def test_transforms():

    kwargs = dict(
        brightness=0.5,
        contrast=0.5,
        saturation=0.4,
        hue=0.2,
        gaussian_prob=0.5,
        solarization_prob=0.4,
    )

    im = np.random.rand(100, 100, 3) * 255
    im = Image.fromarray(im.astype("uint8")).convert("RGB")

    T = prepare_transform("cifar10", multicrop=False, **kwargs)
    assert T(im).size(1) == 32

    T = prepare_transform("stl10", multicrop=False, **kwargs)
    assert T(im).size(1) == 96

    T = prepare_transform("imagenet100", multicrop=False, **kwargs)
    assert T(im).size(1) == 224

    n_crops = 10
    assert len(prepare_n_crop_transform(T, n_crops=n_crops)(im)) == n_crops

    T = prepare_transform("imagenet100", multicrop=True, **kwargs)
    n_crops = [3, 9]
    sizes = [224, 96]
    T = prepare_multicrop_transform(T, sizes, n_crops=n_crops)
    crops = T(im)
    cur = 0
    for i, crop in enumerate(crops):
        assert crop.size(1) == sizes[cur]
        if i + 1 >= n_crops[cur] and len(n_crops) > cur + 1:
            cur += 1


def test_data():

    kwargs = dict(
        brightness=0.5,
        contrast=0.5,
        saturation=0.4,
        hue=0.2,
        gaussian_prob=0.5,
        solarization_prob=0.4,
    )

    T = prepare_transform("cifar10", multicrop=False, **kwargs)
    T = prepare_n_crop_transform(T, n_crops=2)
    train_dataset = prepare_datasets("cifar10", T, data_dir="./datasets")

    assert isinstance(train_dataset, CIFAR10)
    assert len(train_dataset[0]) == 3

    bs = 64
    num_samples_train = len(train_dataset)
    num_batches_train = num_samples_train // bs

    train_loader = prepare_dataloader(train_dataset, batch_size=bs, num_workers=0)

    assert isinstance(train_loader, DataLoader)
    assert num_batches_train == len(train_loader)
