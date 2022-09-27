import torch
from centernet.centernet import CenterNet
import numpy as np

realpath = 'C:/Users/HP/Desktop/detect-system-main'
_default = {"model_path": realpath + '/logs/ep071-loss1.658-val_loss1.688.pth',
            "classes_path": realpath + '/centernet/model_data/voc_classes_ch.txt',
            "backbone": 'resnet50', "input_shape": [512, 512],
            "confidence": 0.3, "nms_iou": 0.3, "nms": True, "letterbox_image": False, "cuda": True}
model = CenterNet(_default).net
model = model.module
model.eval()
input = example = torch.rand(1, 3, 512, 512).cuda()
script = torch.jit.trace(model,input)
script.save('C:/Users/HP/Desktop/detect-system-main/logs/ep071-loss1.658-val_loss1.688.pt')