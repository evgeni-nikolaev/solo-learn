python3 ../../../main_pretrain.py \
    --dataset imagenet100 \
    --encoder resnet18 \
    --data_dir /datasets \
    --train_dir imagenet-100/train \
    --val_dir imagenet-100/val \
    --max_epochs 400 \
    --gpus 0,1 \
    --distributed_backend ddp \
    --sync_batchnorm \
    --precision 16 \
    --optimizer sgd \
    --lars \
    --grad_clip_lars \
    --eta_lars 0.02 \
    --exclude_bias_n_norm \
    --scheduler warmup_cosine \
    --lr 0.3 \
    --weight_decay 1e-4 \
    --batch_size 128 \
    --num_workers 4 \
    --brightness 0.8 \
    --contrast 0.8 \
    --saturation 0.8 \
    --hue 0.2 \
    --name simclr-400ep-imagenet100 \
    --dali \
    --entity unitn-mhug \
    --project solo-learn \
    --wandb \
    --method simclr \
    --temperature 0.2 \
    --proj_hidden_dim 2048

python3 ../../../main_pretrain.py \
    --dataset imagenet100 \
    --encoder resnet18 \
    --data_dir /datasets \
    --train_dir imagenet-100/train \
    --val_dir imagenet-100/val \
    --max_epochs 400 \
    --gpus 0,1 \
    --distributed_backend ddp \
    --sync_batchnorm \
    --precision 16 \
    --optimizer sgd \
    --lars \
    --grad_clip_lars \
    --eta_lars 0.02 \
    --exclude_bias_n_norm \
    --scheduler warmup_cosine \
    --lr 0.3 \
    --weight_decay 1e-4 \
    --batch_size 128 \
    --num_workers 4 \
    --brightness 0.8 \
    --contrast 0.8 \
    --saturation 0.8 \
    --hue 0.2 \
    --multicrop \
    --n_crops 2 \
    --n_small_crops 6 \
    --name multicrop-simclr-400ep-imagenet100 \
    --dali \
    --entity unitn-mhug \
    --project solo-learn \
    --wandb \
    --method simclr \
    --proj_hidden_dim 2048 \
    --temperature 0.1

python3 ../../../main_pretrain.py \
    --dataset imagenet100 \
    --encoder resnet18 \
    --data_dir /datasets \
    --train_dir imagenet-100/train \
    --val_dir imagenet-100/val \
    --max_epochs 400 \
    --gpus 0,1 \
    --distributed_backend ddp \
    --sync_batchnorm \
    --precision 16 \
    --optimizer sgd \
    --optimizer sgd \
    --lars \
    --grad_clip_lars \
    --eta_lars 0.02 \
    --exclude_bias_n_norm \
    --scheduler warmup_cosine \
    --lr 0.3 \
    --weight_decay 1e-4 \
    --batch_size 128 \
    --num_workers 4 \
    --brightness 0.8 \
    --contrast 0.8 \
    --saturation 0.8 \
    --hue 0.2 \
    --multicrop \
    --n_crops 2 \
    --n_small_crops 6 \
    --name multicrop-supervised-simclr-400ep-imagenet100 \
    --dali \
    --entity unitn-mhug \
    --project solo-learn \
    --wandb \
    --method simclr \
    --temperature 0.1 \
    --proj_hidden_dim 2048 \
    --supervised
