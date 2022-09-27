from centernet.centernet import CenterNet
from yolov4.yolo import YOLO
from yolov3_wsm.yolo import YOLO as YOLOV3
import os
from PIL import Image


"""
创建对象
"""
realpath = os.path.realpath(r".")
realpath = realpath.split("\\")
realpath = "/".join(realpath)

_default = {"model_path": realpath + '/logs/ep071-loss1.658-val_loss1.688.pth',
            "classes_path": realpath + '/centernet/model_data/voc_classes_ch.txt',
            "backbone": 'resnet50', "input_shape": [512, 512],
            "confidence": 0.45, "nms_iou": 0.3, "nms": True, "letterbox_image": False, "cuda": True}
centernetModel = CenterNet(_default)


_default = {"model_path": realpath + '/logs/ep043-loss1.984-val_loss1.405.pth',
                             "classes_path": realpath + '/yolov4/model_data/voc_classes.txt',
                             "anchors_path": realpath + '/yolov4/model_data/yolo_anchors.txt',
                             "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]], "input_shape": [416, 416],
                             "confidence": 0.45, "nms_iou": 0.3, "nms": True, "letterbox_image": False, "cuda": True}

yoloModel = YOLO(_default)

_default = {"model_path": realpath + '/logs/ep100-loss4.459-val_loss3.782.pth',
                             "classes_path": realpath + '/yolov3_wsm/model_data/voc_classes.txt',
                             "anchors_path": realpath + '/yolov3_wsm/model_data/yolo_anchors.txt',
                             "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]], "input_shape": [416, 416],
                             "confidence": 0.5, "nms_iou": 0.3, "letterbox_image": False, "cuda": True}
yolo_wsm = YOLOV3(_default)


def predict_image(img_path,model):
    # ----------------------------------------------------------------------------------------------------------#
    #   mode用于指定测试的模式：
    #   'predict'表示单张图片预测，如果想对预测过程进行修改，如保存图片，截取对象等，可以先看下方详细的注释
    #   'video'表示视频检测，可调用摄像头或者视频进行检测，详情查看下方注释。
    #   'fps'表示测试fps，使用的图片是img里面的street.jpg，详情查看下方注释。
    #   'dir_predict'表示遍历文件夹进行检测并保存。默认遍历img文件夹，保存img_out文件夹，详情查看下方注释。
    # ----------------------------------------------------------------------------------------------------------#
    img = img_path
    image, r_image = 0,0
    labels = []
    boxes = []
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
    else:
        r_image, labels, boxes = model.detect_image(image)
        #r_image.show()
    return r_image, labels, boxes
