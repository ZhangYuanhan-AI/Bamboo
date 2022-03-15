#!/bin/sh
# For one model, the name of your model config file
models=(rn50_bamboo_v0_1)
# For multiple models
models=(rn50_bamboo_v0_1, A,B,C)


# datasets=(cifar10)
datasets=(cifar10 cifar100 food pet flower sun car dtd caltech aircraft)


for model in ${models[@]};
do
  echo $model
  for datast in ${datasets[@]};
  do
    echo $datast
    sh run_srun.sh 2 configs/100p/config_${datast}.yaml configs/models_cfg/${model}.yaml ${model}_100p_${datast}
    sleep 10
  done
done
