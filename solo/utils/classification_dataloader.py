import os
from typing import Callable, Optional, Tuple

from torch import nn
import torchvision
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import STL10, ImageFolder


def prepare_transforms(dataset: str) -> Tuple[nn.Module, nn.Module]:
    """Prepares pre-defined train and test transformation pipelines for some datasets.

    Args:
        dataset (str): dataset name.

    Returns:
        Tuple[nn.Module, nn.Module]: training and validation transformation pipelines.
    """

    cifar_pipeline = {
        "T_train": transforms.Compose(
            [
                transforms.RandomResizedCrop(size=32, scale=(0.08, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.247, 0.243, 0.261)),
            ]
        ),
        "T_val": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.247, 0.243, 0.261)),
            ]
        ),
    }

    stl_pipeline = {
        "T_train": transforms.Compose(
            [
                transforms.RandomResizedCrop(size=96, scale=(0.08, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4823, 0.4466), (0.247, 0.243, 0.261)),
            ]
        ),
        "T_val": transforms.Compose(
            [
                transforms.Resize((96, 96)),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4823, 0.4466), (0.247, 0.243, 0.261)),
            ]
        ),
    }

    imagenet_pipeline = {
        "T_train": transforms.Compose(
            [
                transforms.RandomResizedCrop(size=224, scale=(0.08, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.228, 0.224, 0.225)),
            ]
        ),
        "T_val": transforms.Compose(
            [
                transforms.Resize(256),  # resize shorter
                transforms.CenterCrop(224),  # take center crop
                transforms.ToTensor(),
                transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.228, 0.224, 0.225)),
            ]
        ),
    }

    pipelines = {
        "cifar10": cifar_pipeline,
        "cifar100": cifar_pipeline,
        "stl10": stl_pipeline,
        "imagenet100": imagenet_pipeline,
        "imagenet": imagenet_pipeline,
    }

    assert dataset in pipelines

    pipeline = pipelines[dataset]
    T_train = pipeline["T_train"]
    T_val = pipeline["T_val"]

    return T_train, T_val


def prepare_datasets(
    dataset: str,
    T_train: Callable,
    T_val: Callable,
    data_dir: Optional[str] = None,
    train_dir: Optional[str] = None,
    val_dir: Optional[str] = None,
) -> Tuple[Dataset, Dataset]:
    """Prepares train and val datasets.

    Args:
        dataset (str): dataset name.
        T_train (Callable): pipeline of transformations for training dataset.
        T_val (Callable): pipeline of transformations for validation dataset.
        data_dir Optional[str]: path where to download/locate the dataset.
        train_dir Optional[str]: subpath where the training data is located.
        val_dir Optional[str]: subpath where the validation data is located.

    Returns:
        Tuple[Dataset, Dataset]: training dataset and validation dataset.
    """

    if data_dir is None:
        sandbox_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        data_dir = os.path.join(sandbox_dir, "datasets")

    if train_dir is None:
        train_dir = f"{dataset}/train"
    if val_dir is None:
        val_dir = f"{dataset}/val"

    if dataset in ["cifar10", "cifar100"]:
        DatasetClass = vars(torchvision.datasets)[dataset.upper()]
        train_dataset = DatasetClass(
            os.path.join(data_dir, train_dir),
            train=True,
            download=True,
            transform=T_train,
        )

        val_dataset = DatasetClass(
            os.path.join(data_dir, val_dir),
            train=False,
            download=True,
            transform=T_val,
        )

    elif dataset == "stl10":
        train_dataset = STL10(
            os.path.join(data_dir, train_dir),
            split="train",
            download=True,
            transform=T_train,
        )
        val_dataset = STL10(
            os.path.join(data_dir, val_dir),
            split="test",
            download=True,
            transform=T_val,
        )

    elif dataset in ["imagenet", "imagenet100"]:
        train_dir = os.path.join(data_dir, train_dir)
        val_dir = os.path.join(data_dir, val_dir)

        train_dataset = ImageFolder(train_dir, T_train)
        val_dataset = ImageFolder(val_dir, T_val)

    return train_dataset, val_dataset


def prepare_dataloaders(
    train_dataset: Dataset, val_dataset: Dataset, batch_size: int = 64, num_workers: int = 4
) -> Tuple[DataLoader, DataLoader]:
    """Wraps a train and a validation dataset with a DataLoader.

    Args:
        train_dataset (Dataset): object containing training data.
        val_dataset (Dataset): object containing validation data.
        batch_size (int): batch size.
        num_workers (int): number of parallel workers.
    Returns:
        Tuple[DataLoader, DataLoader]: training dataloader and validation dataloader.
    """

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=True,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=False,
    )
    return train_loader, val_loader


def prepare_data(
    dataset: str,
    data_dir: Optional[str] = None,
    train_dir: Optional[str] = None,
    val_dir: Optional[str] = None,
    batch_size: int = 64,
    num_workers: int = 4,
) -> Tuple[DataLoader, DataLoader]:
    """Prepares transformations, creates dataset objects and wraps them in dataloaders.

    Args:
        dataset (str): dataset name.
        data_dir (Optional[str], optional): path where to download/locate the dataset.
            Defaults to None.
        train_dir (Optional[str], optional): subpath where the training data is located.
            Defaults to None.
        val_dir (Optional[str], optional): subpath where the validation data is located.
            Defaults to None.
        batch_size (int, optional): batch size. Defaults to 64.
        num_workers (int, optional): number of parallel workers. Defaults to 4.

    Returns:
        Tuple[DataLoader, DataLoader]: prepared training and validation dataloader;.
    """

    T_train, T_val = prepare_transforms(dataset)
    train_dataset, val_dataset = prepare_datasets(
        dataset,
        T_train,
        T_val,
        data_dir=data_dir,
        train_dir=train_dir,
        val_dir=val_dir,
    )
    train_loader, val_loader = prepare_dataloaders(
        train_dataset,
        val_dataset,
        batch_size=batch_size,
        num_workers=num_workers,
    )
    return train_loader, val_loader
