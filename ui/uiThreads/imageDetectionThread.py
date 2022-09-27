import time
import warnings
from collections import defaultdict

from centernet.centernet import CenterNet
import PIL
import cv2
import numpy as np
from PIL import Image
from PIL import ImageQt
from PIL.Image import fromqpixmap

import matplotlib.pyplot as plt
from PIL.Image import Image
from centernet import predict as predict_centernet
from yolov4 import predict as predict_yolov4
from yolov3_wsm import predict as predict_yolov3
from PyQt5.QtCore import pyqtSignal, QThread


class ImageDetectionThread(QThread):
    infoEmit = pyqtSignal(str, str)
    overEmit = pyqtSignal()

    def __init__(self):
        super(ImageDetectionThread, self).__init__()

    def setPara(self, *args):
        self.imagePath = args[0]
        self.detectMode = args[1]
        self._default = args[2]
        self.temp_path = "./result.jpg"

    def run(self) -> None:
        self._sendInfo("T", "子线程已开启....")
        print("子线程已开启....")
        # try:
        #     # 预启动模型

        if self.detectMode == "yolov4":
            image, labels, boxes = predict_yolov4.predict_image(self.imagePath, self._default)
        elif self.detectMode == "yolov3":
            image, labels, boxes = predict_yolov3.predict_image(self.imagePath, self._default)
        else:
            image, labels, boxes = predict_centernet.predict_image(self.imagePath, self._default)
        image.save(self.temp_path)
        if labels == []:
            labels = "null"
        self._sendInfo("A", labels)
        # 结束，发送终止信号
        self.overEmit.emit()
        # except Exception as e:
        #     self._sendInfo("E", "异常警告：" + e.__str__())

    def _sendInfo(self, type, infoStr):
        self.infoEmit.emit(type, infoStr)

    def killThread(self):
        """
        结束线程
        :return:
        """
        self.terminate()