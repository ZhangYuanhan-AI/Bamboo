## Bamboo: Building Mega-Scale Vision Dataset Continually with Human-Machine Synergy

![fig1](Figures/Fig1.png)

[[Paper](https://arxiv.org/abs/2203.07845)][[Project](https://opengvlab.shlab.org.cn/bamboo/home)]  

[Zhang Yuanhan](https://github.com/Davidzhangyuanhan/Bamboo), [Sun Qinghong](https://github.com/Davidzhangyuanhan/Bamboo), [Zhou Yichun](https://github.com/Davidzhangyuanhan/Bamboo), [He Zexin](https://scholar.google.com/citations?user=FVPnSPcAAAAJ&hl=zh-CN&oi=ao), [Yin Zhenfei](https://scholar.google.com.hk/citations?user=ngPR1dIAAAAJ&hl=zh-CN), [Wang Kun](https://twitter.com/wk910930), [Qiao Yu](http://mmlab.siat.ac.cn/yuqiao), [Shao Jing](https://amandajshao.github.io/), [Liu Ziwei](https://liuziwei7.github.io/)

> Abstract: Large-scale datasets play a vital role in computer vision. Existing datasets are either collected according to heuristic label systems or annotated blindly without differentiation to samples, making them inefficient and unscalable. How to systematically collect, annotate and build a mega-scale dataset remains an open question. In this work, we advocate building a high-quality vision dataset actively and continually on a comprehensive label system.
Specifically, we contribute **Bamboo** Dataset, a mega-scale and information-dense dataset for both classification and detection. 
It is built upon this human-machine synergy with two appealing properties:

>  **1) Label System:** we integrate categories from 24 public datasets and collect 170,586 new categories from knowledge bases, forming a hierarchical label system with 304,048 categories. The label system is easily extendable under our designed hierarchy, and its concepts are further distinguished as ''visual'' or ''non-visual''.

>  **2) Active Annotation:** based on a real-world data pool of 370M raw images crawled by the label system, only informative samples are selected for manual labeling through our human-machine active annotation framework. We find that rectifying out-of-distribution samples is crucial for active learning to function in realistic scenarios.
Bamboo aims to populate these comprehensive categories with 69M image classification annotations and 170,586 object bounding box annotations. 
Compared to ImageNet22K and Objects365, models pre-trained on Bamboo achieve superior performance among various downstream tasks (6.2% gains on classification and 2.1% gains on detection). In addition, we provide valuable observations regarding large-scale pre-training from over 1,000 experiments.
Due to its scalable nature on both label system and annotation pipeline, Bamboo will continue to grow and benefit from the collective efforts of the community, which we hope would pave the way for more general vision models. 


## Updates
[03/2022] Bamboo-CLS ResNet-50 and Bamboo-CLS ViT B/16 have been **released**.

[03/2022] [arXiv](https://arxiv.org/abs/2203.07845) paper has been **released**.

## Dataset

### Explore
[Website Link](https://opengvlab.shlab.org.cn/bamboo/home)

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
| Model     | Link                                                                                         | Data       | cifar10 | cifar100 | food  | pet   | flower | sun   | stanfordcar | dtd   | caltech | fgvc-aircraft | AVG       |
|-----------|----------------------------------------------------------------------------------------------|------------|---------|----------|-------|-------|--------|-------|-------------|-------|---------|---------------|-----------|
| ResNet-50 | Official                                                                                     | CLIP       |    88.7 |     70.3 |  86.4 |  88.2 |   96.1 |  73.3 |        78.3 |  76.4 |    89.6 |          49.1 | 79.64     |
| ViT B/16  | Official                                                                                     | CLIP       |    96.2 |     83.1 |  92.8 |  93.1 |   98.1 |  78.4 |        86.7 |  79.2 |    94.7 |          59.5 | 86.18     |
| ResNet-50 | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) | Bamboo-CLS | 93.6   | 81.7    | 85.6 | 93.0 | 99.4  | 71.6 | 92.3       | 78.2 | 93.6   | 84.4          | **87.33** |
| ViT B/16  | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) | Bamboo-CLS |   98.5 |    91.0 | 93.3 | 95.3 |  99.7 | 79.5 |       93.9 | 81.9 |   94.8 |          88.8 | **91.65** |

### Bamboo-DET (TBA)

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

Thanks Chen Siyu (https://github.com/Siyu-C) for implementing the Bamboo-Benchmark.

## Citation
If you use this code in your research, please kindly cite the following papers.

```
@misc{zhang2022bamboo,
      title={Bamboo: Building Mega-Scale Vision Dataset Continually with Human-Machine Synergy}, 
      author={Yuanhan Zhang and Qinghong Sun and Yichun Zhou and Zexin He and Zhenfei Yin and Kun Wang and Lu Sheng and Yu Qiao and Jing Shao and Ziwei Liu},
      year={2022},
      eprint={2203.07845},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


