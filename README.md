## Bamboo: Building Mega-Scale Vision Dataset Continually with Human-Machine Synergy

![fig1](Figures/Fig1.png)

[[paper](https://arxiv.org/abs/2007.12342)] 

[Zhang Yuanhan](https://github.com/Davidzhangyuanhan/Bamboo), [Sun Qinghong](https://github.com/Davidzhangyuanhan/Bamboo), [Zhou Yichun](https://github.com/Davidzhangyuanhan/Bamboo), [He Zexin](https://scholar.google.com/citations?user=FVPnSPcAAAAJ&hl=zh-CN&oi=ao), [Shao Jing](https://amandajshao.github.io/), [Liu Ziwei](https://liuziwei7.github.io/), *et.al* 

> Abstract: Large-scale datasets play a vital role in computer vision. Existing datasets are either collected according to heuristic label systems or annotated blindly without differentiation to samples, making them inefficient and unscalable. How to systematically collect, annotate and build a mega-scale dataset remains an open question. In this work, we advocate building a high-quality vision dataset actively and continually on a comprehensive label system.
Specifically, we contribute **Bamboo** Dataset, a mega-scale and information-dense dataset for both classification and detection. 
It is built upon this human-machine synergy with two appealing properties:

>  **1) Label System:** we integrate categories from 24 public datasets and collect 170,586 new categories from knowledge bases, forming a hierarchical label system with 304,048 categories. The label system is easily extendable under our designed hierarchy, and its concepts are further distinguished as ''visual'' or ''non-visual''.

>  **2) Active Annotation:** based on a real-world data pool of 370M raw images crawled by the label system, only informative samples are selected for manual labeling through our human-machine active annotation framework. We find that rectifying out-of-distribution samples is crucial for active learning to function in realistic scenarios.
Bamboo aims to populate these comprehensive categories with 24 image classification annotations and 170,586 object bounding box annotations. 
Compared to ImageNet22K and Objects365, models pre-trained on Bamboo achieve superior performance among various downstream tasks (6.2% gains on classification and 2.1% gains on detection). In addition, we provide valuable observations regarding large-scale pre-training from over 1,000 experiments.
Due to its scalable nature on both label system and annotation pipeline, Bamboo will continue to grow and benefit from the collective efforts of the community, which we hope would pave the way for more general vision models. 


## Updates
[03/2022] Bamboo-CLS ResNet-50 and Bamboo-CLS ViT B/16 have been **released**.

[03/2022] arxiv paper have been **released**.

## Dataset Explore and Downloads

### Explore
[website link](https://opengvlab.shlab.org.cn/bamboo/home)

### Downloads
1. Sign up an account at [HERE](https://opengvlab.shlab.org.cn/register?redirect=/home), get the *USERNAME* for *opengvlab*.
2. Send your request to opengvlab@pjlab.org.cn. The request should include your name, username and orgnization as follows. We will notify you by email as soon as possible.
```
USERNANE: USERNANE(from step1)
NAME: XXX
ORGANIZATION: XXX (Bamboo is only for academic research and non-commercial use)
```

## Model Zoo

### Bamboo-CLS
| Model     | Link                                                                                         | cifar10 | cifar100 | food  | pet   | flower | sun   | stanfordcar | dtd   | caltech | fgvc-aircraft | AVG   |
|-----------|----------------------------------------------------------------------------------------------|---------|----------|-------|-------|--------|-------|-------------|-------|---------|---------------|-------|
| ResNet-50 | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) | 93.58   | 81.65    | 85.58 | 92.95 | 99.44  | 71.62 | 92.29       | 78.19 | 93.63   | 84.4 | 87.33 |
| ViT B/16  | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) |   98.48 |    90.99 | 93.28 | 95.26 |  99.71 | 79.45 |       93.86 | 81.91 |   94.77 | 88.8 | 91.65 |

### Bamboo-DET (TBD)

## Linear Probe
### Step 1: 
Downloading and organizing each downstream dataset as follows

```
mmclassification (take flowers for example)
├── data
│   ├── flowers
│   │   ├── train/
│   │   ├── test/
│   │   ├── train_meta.list
│   │   ├── test_meta.list
```
### Step 2: 
Changing root and meta in *Bamboo-Benchmark/configs/100p/config_\*.yaml*

### Step 3:
Writing the path of the downloaded/your model config in 

*Bamboo-Benchmark/configs/models_cfg/\*.yaml*

### Step 4:
Writing the name of the downloaded/your model in *Bamboo-Benchmark/multi_run_100p.sh*

### Step 5:
sh *Bamboo-Benchmark/multi_run_100p.sh*

## Acknowledgement

Thanks, Chen Siyu(https://github.com/Siyu-C), for implementing the Bamboo-Benchmark.

