<div align="center">

[![tests](https://github.com/vturrisi/solo-learn/actions/workflows/tests.yml/badge.svg)](https://github.com/vturrisi/solo-learn/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/solo-learn/badge/?version=latest)](https://solo-learn.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/vturrisi/solo-learn/branch/main/graph/badge.svg?token=WLU9UU17XZ)](https://codecov.io/gh/vturrisi/solo-learn)

</div>

# solo-learn

A library of self-supervised methods for unsupervised visual representation learning powered by PyTorch Lightning.
We aim at providing SOTA self-supervised methods in a comparable environment while, at the same time, implementing training tricks.
While the library is self contained, it is possible to use the models outside of solo-learn.

---

## Methods available:

* [Barlow Twins](https://arxiv.org/abs/2103.03230)
* [BYOL](https://arxiv.org/abs/2006.07733)
* [DINO](https://arxiv.org/abs/2104.14294)
* [MoCo V2+](https://arxiv.org/abs/2003.04297)
* [NNCLR](https://arxiv.org/abs/2104.14548)
* [SimCLR](https://arxiv.org/abs/2002.05709) + [Supervised Contrastive Learning](https://arxiv.org/abs/2004.11362)
* [SimSiam](https://arxiv.org/abs/2011.10566)
* [Swav](https://arxiv.org/abs/2006.09882)
* [VICReg](https://arxiv.org/abs/2105.04906)
* [W-MSE](https://arxiv.org/abs/2007.06346)

---

## Extra flavor

### Data
* Increased data processing speed by up to 100% using [Nvidia Dali](https://github.com/NVIDIA/DALI)
* Asymmetric and symmetric augmentations
### Evaluation and logging
* Online linear evaluation via stop-gradient for easier debugging and prototyping (optionally available for the momentum encoder as well)
* Normal offline linear evaluation
* All the perks of PyTorch Lightning (mixed precision, gradient accumulation, clipping, automatic logging and much more)
* Easy-to-extend modular code structure
* Custom model logging with a simpler file organization
* Common metrics and more to come (auto TSNE)
### Training tricks
* Multi-cropping dataloading following [SwAV](https://arxiv.org/abs/2006.09882):
    * **Note**: currently, only SimCLR supports this
* Exclude batchnorm and biases from LARS
* No LR scheduler for the projection head in SimSiam
---
## Requirements

* torch
* tqdm
* einops
* wandb
* pytorch-lightning
* lightning-bolts

**Optional**:
* nvidia-dali

**NOTE:** if you are using CUDA 10.X use `nvidia-dali-cuda100` in `requirements.txt`.

---

## Installation

To install the repository with dali support, use:
```
pip3 install .[dali]
```

If no dali support is needed, the repository can be installed as:
```
pip3 install .
```

**NOTE:** If you want to modify the library, install it in dev mode with `-e`.

**NOTE 2:** Soon to be on pip.

---

## Training

For pretraining the encoder, follow one of the many bash files in `bash_files/pretrain/`.

After that, for offline linear evaluation, follow the examples on `bash_files/linear`.

**NOTE:** Files try to be up-to-date and follow as closely as possible the recommended parameters of each paper, but check them before running.

---

## Results

**Note:** hyperparameters may not be the best, we will be re-running the methods with lower performance eventually.

### CIFAR-10

| Method       | Backbone | Epochs | Dali | Acc@1 (online) | Acc@1 (offline) | Acc@5 (online) | Acc@5 (offline) | Checkpoint |
|--------------|:--------:|:------:|:----:|:--------------:|:---------------:|:--------------:|:---------------:|:----------:|
| Barlow Twins | ResNet18 |  1000  |  :x: |      92.10     |                 |     99.73      |                 | [:link:](https://drive.google.com/drive/folders/1L5RAM3lCSViD2zEqLtC-GQKVw6mxtxJ_?usp=sharing) |
| BYOL         | ResNet18 |  1000  |  :x: |      92.58     |                 |     99.79      |                 | [:link:](https://drive.google.com/drive/folders/1KxeYAEE7Ev9kdFFhXWkPZhG-ya3_UwGP?usp=sharing) |
| DINO         | ResNet18 |  1000  |  :x: |      89.52     |                 |     99.71      |                 | [:link:](https://drive.google.com/drive/folders/1vyqZKUyP8sQyEyf2cqonxlGMbQC-D1Gi?usp=sharing) |
| MoCo V2+     | ResNet18 |  1000  |  :x: |      92.94     |                 |     99.79      |                 | [:link:](https://drive.google.com/drive/folders/1ruNFEB3F-Otxv2Y0p62wrjA4v5Fr2cKC?usp=sharing) |
| NNCLR        | ResNet18 |  1000  |  :x: |      91.88     |                 |     99.78      |                 | [:link:](https://drive.google.com/drive/folders/1xdCzhvRehPmxinphuiZqFlfBwfwWDcLh?usp=sharing) |
| SimCLR       | ResNet18 |  1000  |  :x: |      90.74     |                 |     99.75      |                 | [:link:](https://drive.google.com/drive/folders/1mcvWr8P2WNJZ7TVpdLHA_Q91q4VK3y8O?usp=sharing) |
| Simsiam      | ResNet18 |  1000  |  :x: |      90.51     |                 |     99.72      |                 | [:link:](https://drive.google.com/drive/folders/1OO_igM3IK5oDw7GjQTNmdfg2I1DH3xOk?usp=sharing) |
| SwAV         | ResNet18 |  1000  |  :x: |      89.17     |                 |     99.68      |                 | [:link:](https://drive.google.com/drive/folders/1nlJH4Ljm8-5fOIeAaKppQT6gtsmmW1T0?usp=sharing) |
| VICReg       | ResNet18 |  1000  |  :x: |      92.07     |                 |     99.74      |                 | [:link:](https://drive.google.com/drive/folders/159ZgCxocB7aaHxwNDubnAWU71zXV9hn-?usp=sharing) |
| W-MSE        | ResNet18 |  1000  |  :x: |      88.67     |                 |     99.68      |                 | [:link:](https://drive.google.com/drive/folders/1xPCiULzQ4JCmhrTsbxBp9S2jRZ01KiVM?usp=sharing) |


### CIFAR-100

| Method       | Backbone | Epochs | Dali | Acc@1 (online) | Acc@1 (offline) | Acc@5 (online) | Acc@5 (offline) | Checkpoint |
|--------------|:--------:|:------:|:----:|:--------------:|:---------------:|:--------------:|:---------------:|:----------:|
| Barlow Twins | ResNet18 |  1000  |  :x: |      70.90     |                 |     91.91      |                 | [:link:](https://drive.google.com/drive/folders/1hDLSApF3zSMAKco1Ck4DMjyNxhsIR2yq?usp=sharing) |
| BYOL         | ResNet18 |  1000  |  :x: |      70.46     |                 |     91.96      |                 | [:link:](https://drive.google.com/drive/folders/1hwsEdsfsUulD2tAwa4epKK9pkSuvFv6m?usp=sharing) |
| DINO         | ResNet18 |  1000  |  :x: |      66.76     |                 |     90.34      |                 | [:link:](https://drive.google.com/drive/folders/1TxeZi2YLprDDtbt_y5m29t4euroWr1Fy?usp=sharing) |
| MoCo V2+     | ResNet18 |  1000  |  :x: |      69.89     |                 |     91.65      |                 | [:link:](https://drive.google.com/drive/folders/15oWNM16vO6YVYmk_yOmw2XUrFivRXam4?usp=sharing) |
| NNCLR        | ResNet18 |  1000  |  :x: |      69.62     |                 |     91.52      |                 | [:link:](https://drive.google.com/drive/folders/1Dz72o0-5hugYPW1kCCQDBb0Xi3kzMLzu?usp=sharing) |
| SimCLR       | ResNet18 |  1000  |  :x: |      65.78     |                 |     89.04      |                 | [:link:](https://drive.google.com/drive/folders/13pGPcOO9Y3rBoeRVWARgbMFEp8OXxZa0?usp=sharing) |
| Simsiam      | ResNet18 |  1000  |  :x: |      66.04     |                 |     89.62      |                 | [:link:](https://drive.google.com/drive/folders/1AJUPmsIHh_nqEcFe-Vcz2o4ruEibFHWO?usp=sharing) |
| SwAV         | ResNet18 |  1000  |  :x: |      64.88     |                 |     88.78      |                 | [:link:](https://drive.google.com/drive/folders/1U_bmyhlPEN941hbx0SdRGOT4ivCarQB9?usp=sharing) |
| VICReg       | ResNet18 |  1000  |  :x: |      68.54     |                 |     90.83      |                 | [:link:](https://drive.google.com/drive/folders/1AHmVf_Zl5fikkmR4X3NWlmMOnRzfv0aT?usp=sharing) |
| W-MSE        | ResNet18 |  1000  |  :x: |      61.33     |                 |     87.26      |                 | [:link:](https://drive.google.com/drive/folders/1vc9j3RLpVCbECh6o-44oMiE5snNyKPlF?usp=sharing) |

### ImageNet-100

| Method                  | Backbone | Epochs |        Dali        | Acc@1 (online) | Acc@1 (offline) | Acc@5 (online) | Acc@5 (offline) | Checkpoint |
|-------------------------|:--------:|:------:|:------------------:|:--------------:|:---------------:|:--------------:|:---------------:|:----------:|
| Barlow Twins :rocket:   | ResNet18 |   400  | :heavy_check_mark: |      80.38     |     80.16       |      95.28     |      95.14      | [:link:](https://drive.google.com/drive/folders/1rj8RbER9E71mBlCHIZEIhKPUFn437D5O?usp=sharing) |
| BYOL         :rocket:   | ResNet18 |   400  | :heavy_check_mark: |      79.76     |     80.16       |      94.80     |      95.14      | [:link:](https://drive.google.com/drive/folders/1riOLjMawD_znO4HYj8LBN2e1X4jXpDE1?usp=sharing) |
| DINO                    | ResNet18 |   400  | :heavy_check_mark: |      74.84     |     74.92       |      92.92     |      92.78      | [:link:](https://drive.google.com/drive/folders/1NtVvRj-tQJvrMxRlMtCJSAecQnYZYkqs?usp=sharing) |
| MoCo V2+     :rocket:   | ResNet18 |   400  | :heavy_check_mark: |      78.20     |     79.28       |      95.50     |      95.18      | [:link:](https://drive.google.com/drive/folders/1ItYBtMJ23Yh-Rhrvwjm4w1waFfUGSoKX?usp=sharing) |
| NNCLR        :rocket:   | ResNet18 |   400  | :heavy_check_mark: |      79.80     |     80.16       |      95.28     |      95.30      | [:link:](https://drive.google.com/drive/folders/1QMkq8w3UsdcZmoNUIUPgfSCAZl_LSNjZ?usp=sharing) |
| SimCLR       :rocket:   | ResNet18 |   400  | :heavy_check_mark: |      77.04     |     77.48       |      94.02     |      93.42      | [:link:](https://drive.google.com/drive/folders/1yxAVKnc8Vf0tDfkixSB5mXe7dsA8Ll37?usp=sharing) |
| Simsiam                 | ResNet18 |   400  | :heavy_check_mark: |      74.54     |     78.72       |      93.16     |      94.78      | [:link:](https://drive.google.com/drive/folders/1Bc8Xj-Z7ILmspsiEQHyQsTOn4M99F_f5?usp=sharing) |
| SwAV                    | ResNet18 |   400  | :heavy_check_mark: |      74.04     |     74.28       |      92.70     |      92.84      | [:link:](https://drive.google.com/drive/folders/1VWCMM69sokzjVoPzPSLIsUy5S2Rrm1xJ?usp=sharing) |
| VICReg       :rocket: | ResNet18 |   400  | :heavy_check_mark: |      79.22     |       79.40       |      95.06     |      95.02      | [:link:](https://drive.google.com/drive/folders/1uWWR5VBUru8vaHaGeLicS6X3R4CfZsr2?usp=sharing) |
| W-MSE                   | ResNet18 |   400  | :heavy_check_mark: |      67.60     |     69.06       |      90.94     |      91.22      | [:link:](https://drive.google.com/drive/folders/1TxubagNV4z5Qs7SqbBcyRHWGKevtFO5l?usp=sharing) |

:rocket: methods where hyperparameters were heavily tuned.

### ImageNet

| Method       | Backbone | Epochs |        Dali        | Acc@1 (online) | Acc@1 (offline) | Acc@5 (online) | Acc@5 (offline) | Checkpoint |
|--------------|:--------:|:------:|:------------------:|:--------------:|:---------------:|:--------------:|:---------------:|:----------:|
| Barlow Twins | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| BYOL         | ResNet50 |   100  | :heavy_check_mark: |      68.62     |      68.36      |      88.90     |       66.66     | [:link:](https://drive.google.com/drive/folders/1-UXo-MttdrqiEQXfV4Duc93fA3mIdsha?usp=sharing) |
| DINO         | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| MoCo V2+     | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| NNCLR        | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| SimCLR       | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| Simsiam      | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| SwAV         | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| VICReg       | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |
| W-MSE        | ResNet50 |   100  | :heavy_check_mark: |                |                 |                |                 |            |


## Training efficiency for DALI

We report the training efficiency of some methods using a ResNet18 with and without DALI in a server with an Intel i9-9820X and two RTX2080ti.

| Method       |  Dali  |  Total time for 20 epochs  |  Time for a 1 epoch |  GPU memory (per GPU) |
|--------------|:------:|:--------------------------:|:-------------------:|:---------------------:|
| Barlow Twins | :x:              | 1h 38m 27s |  4m 55s              |      5097 MB     |
|              |:heavy_check_mark:| 43m 2s     |  2m 10s (56% faster) |      9292 MB     |
| BYOL         | :x:              | 1h 38m 46s |  4m 56s              |      5409 MB     |
|              |:heavy_check_mark:| 50m 33s    |  2m 31s (49% faster) |      9521 MB     |
| NNCLR        | :x:              | 1h 38m 30s |  4m 55s              |      5060 MB     |
|              |:heavy_check_mark:| 42m 3s     |  2m 6s  (64% faster) |      9244 MB     |

**Note**: GPU memory increase doesn't scale with the model.

---

## Citation
If you use solo-learn, please cite our preprint:
```
@misc{turrisi2021solo,
  author =       {Victor G. Turrisi da Costa and Enrico Fini and Nicu Sebe and Elisa Ricci},
  title =        {solo-learn: A Library of Self-supervised Methods for Visual Representation Learning},
  howpublished = {\url{https://github.com/vturrisi/solo-learn}},
  year =         {2021}
}
```
