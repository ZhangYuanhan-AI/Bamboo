import timm

import torch
import copy
import torch.nn as nn
from pycls.models import effnet



class efficientnet(nn.Module):
    def __init__(self, model_name):
        super().__init__()
        # print('initializing ViT model as backbone using ckpt:', clip_pretrain_path)
        # self.model = timm.create_model('vit_base_patch16_224',checkpoint_path=clip_pretrain_path,num_classes=num_classes)# pretrained=True)
        model_name = model_name.split("_")[1].upper()
        assert model_name in ["B{}".format(i) for i in range(8)]
        backbone = effnet(model_name, pretrained=True)
        backbone.head.fc = torch.nn.Identity()

    

    def forward(image):
        # EfficientNet models from pycls are trained in BGR order
        # https://github.com/facebookresearch/pycls/blob/b314d43e918ad8763c5882730ad55a1eef5e8347/pycls/datasets/imagenet.py#L87
        image = torch.flip(image, [1])
        return backbone(image)

    

def efficientnet_B4(**kwargs):
    """Constructs a ResNet-50 model.
    """
    model = efficientnet('efficientnet_B4')
    return model