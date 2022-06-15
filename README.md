![fig1](Figures/teaser.png)

<div align="center">

[Zhang Yuanhan](https://github.com/Davidzhangyuanhan/Bamboo), [Sun Qinghong](https://github.com/Davidzhangyuanhan/Bamboo), [Zhou Yichun](https://github.com/Davidzhangyuanhan/Bamboo), [He Zexin](https://scholar.google.com/citations?user=FVPnSPcAAAAJ&hl=zh-CN&oi=ao), [Yin Zhenfei](https://scholar.google.com.hk/citations?user=ngPR1dIAAAAJ&hl=zh-CN), [Wang Kun](https://twitter.com/wk910930), [Qiao Yu](http://mmlab.siat.ac.cn/yuqiao), [Shao Jing](https://amandajshao.github.io/), [Liu Ziwei](https://liuziwei7.github.io/)


<img src="Figures/teaser_annimation.gif" alt="Pineapple" style="width:360px;height:200px;float:right;margin-top:10px">

<h3>TL;DR</h3>


Bamboo is a mega-scale and information-dense dataset for classification and detection pre-training. It is built upon integrating 24 public datasets (e.g. ImagenNet, Places365, Object365, OpenImages) and added new annotations through active learning. Bamboo has 69M image classification annotations (<span style="color:#AE2011">**4 times larger than ImageNet**</span>) and 32M object bounding boxes (<span style="color:#AE2011">**2 times larger than Object365**</span>).


---

<div>
    <a href='https://arxiv.org/abs/2203.07845' target='_blank'>[Paper]</a>•
    <a href='https://opengvlab.shlab.org.cn/bamboo/home' target='_blank'>[Project]</a>
</div>
</div>

## Leaderboard
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/image-classification-on-dtd)](https://paperswithcode.com/sota/image-classification-on-dtd?p=bamboo-building-mega-scale-vision-dataset) :partying_face:!\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/image-classification-on-food-101-1)](https://paperswithcode.com/sota/image-classification-on-food-101-1?p=bamboo-building-mega-scale-vision-dataset) :partying_face:!\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/fine-grained-image-classification-on-sun397)](https://paperswithcode.com/sota/fine-grained-image-classification-on-sun397?p=bamboo-building-mega-scale-vision-dataset)\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/image-classification-on-flowers-102)](https://paperswithcode.com/sota/image-classification-on-flowers-102?p=bamboo-building-mega-scale-vision-dataset)\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/fine-grained-image-classification-on-caltech)](https://paperswithcode.com/sota/fine-grained-image-classification-on-caltech?p=bamboo-building-mega-scale-vision-dataset)\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/fine-grained-image-classification-on-oxford-1)](https://paperswithcode.com/sota/fine-grained-image-classification-on-oxford-1?p=bamboo-building-mega-scale-vision-dataset) \
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/image-classification-on-cifar-100)](https://paperswithcode.com/sota/image-classification-on-cifar-100?p=bamboo-building-mega-scale-vision-dataset)\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/fine-grained-image-classification-on-stanford)](https://paperswithcode.com/sota/fine-grained-image-classification-on-stanford?p=bamboo-building-mega-scale-vision-dataset)\
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/bamboo-building-mega-scale-vision-dataset/image-classification-on-cifar-10)](https://paperswithcode.com/sota/image-classification-on-cifar-10?p=bamboo-building-mega-scale-vision-dataset)

## Updates
[03/2022] Bamboo-CLS ResNet-50 and Bamboo-CLS ViT B/16 have been **released**.

[03/2022] [arXiv](https://arxiv.org/abs/2203.07845) paper has been **released**.

## About Bamboo

### Explore
[Website Link](https://opengvlab.shlab.org.cn/bamboo/home)

### Downloads
- Sign up an account at [HERE](https://opengvlab.shlab.org.cn/register?redirect=/home), get the *USERNAME* for *opengvlab*.
- Send your request to opengvlab@pjlab.org.cn. The request should include your name, username and orgnization as follows. We will notify you by email as soon as possible.
    ```
    USERNANE: USERNANE(from step1)
    NAME: XXX
    ORGANIZATION: XXX (Bamboo is only for academic research and non-commercial use)
    ```

### Label sytem
We provide the hierarchy for our label system at [HERE](https://drive.google.com/drive/folders/1Eq76P57xjKiqas-JdEy9zSTbtC-YdtKw?usp=sharing). This JSON file includes the following **attrubutes** of each concept. We hope this information will be beneficial for your research.

We take concept/class ``dog`` as an example.
- Load JSON file
    ```
    #input
    with open('PATH-TO-JSON-FILE.json') as f:
    bamboo = json.load(f)
    print(bamboo.keys())
    ```
    ```
    #output
    'father2child', 'child2father', 'id2name', 'id2desc', 'id2desc_zh', 'id2name_zh'
    ```
- Check the ``id (n02084071)`` of the ``dog`` on [HERE](https://opengvlab.shlab.org.cn/bamboo/search).
- Get the **attrubutes** you need.
    - Hypernyms ``bamboo['child2father']['n02084071']``: domestic_animals, canine.
    - Hyponyms ``bamboo['father2child']['n02084071']``: husky, griffon, shiba inu and etc.
    - Description ``bamboo['id2desc']['n02084071']``: a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds.
    - Included in which public dataset ``bamboo['id2state']['n02084071']['academic']``: openimage, iWildCam2020, STL10, cifar10, iNat2021, ImageNet21K, coco, OpenImage object365.

<img src="Figures/json_annimation.gif" alt="Pineapple">








### Special meta file
Downloading the whole dataset might be unnecessary for most purposes. We provide meta files based on the following dimension.
- [ ] Class-wise (e.g. dog, car, boat and etc.)
- [ ] Superclass-wise (e.g. animal, transportation, structure and etc.)



## Model Zoo

### Bamboo-CLS
| Model     | Link                                                                                         | Data       | cifar10 | cifar100 | food  | pet   | flower | sun   | stanfordcar | dtd   | caltech | fgvc-aircraft | AVG       |
|-----------|----------------------------------------------------------------------------------------------|------------|---------|----------|-------|-------|--------|-------|-------------|-------|---------|---------------|-----------|
| ResNet-50 | Official                                                                                     | CLIP       |    88.7 |     70.3 |  86.4 |  88.2 |   96.1 |  73.3 |        78.3 |  76.4 |    89.6 |          49.1 | 79.64     |
| ViT B/16  | Official                                                                                     | CLIP       |    96.2 |     83.1 |  92.8 |  93.1 |   98.1 |  78.4 |        86.7 |  79.2 |    94.7 |          59.5 | 86.18     |
| ResNet-50 | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) | Bamboo-CLS | 93.6   | 81.7    | 85.6 | 93.0 | 99.4  | 71.6 | 92.3       | 78.2 | 93.6   | 84.4          | **87.33** |
| ViT B/16  | [link](https://drive.google.com/drive/folders/1OlKVwzF5N3jwBkOmZ2QBloIeK1GrjakE?usp=sharing) | Bamboo-CLS |   98.5 |    91.0 | 93.3 | 95.3 |  99.7 | 79.5 |       93.9 | 81.9 |   94.8 |          88.8 | **91.65** |

### Bamboo-DET (TBA)

## Getting Started

### Installation
```
# Create conda environment
conda create -n bamboo python=3.7
conda activate bamboo

# Install Pytorch
conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=10.2 -c pytorch

# Clone and install
git clone https://github.com/Davidzhangyuanhan/Bamboo.git
```
### Linear Probe
#### Step 1: 
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
#### Step 2: 
Changing root and meta in *Bamboo-Benchmark/configs/100p/config_\*.yaml*

#### Step 3:
Writing the path of the downloaded/your model config in 

*Bamboo-Benchmark/configs/models_cfg/\*.yaml*

#### Step 4:
Writing the name of the downloaded/your model in *Bamboo-Benchmark/multi_run_100p.sh*

#### Step 5:
sh *Bamboo-Benchmark/multi_run_100p.sh*

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

## Acknowledgement

Thanks Chen Siyu (https://github.com/Siyu-C) for implementing the Bamboo-Benchmark.


