# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagesDetectionWight.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import  os
from PIL import Image
from ui.uiThreads import imageDetectionThread

class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)
    def setupUi(self, Form):
        self.realpath = os.path.realpath(r".")
        self.realpath = self.realpath.split("\\")
        self.realpath = "/".join(self.realpath)
        self._default = {"model_path": self.realpath + '/logs/ep100-loss4.459-val_loss3.782.pth',
                             "classes_path": self.realpath + '/yolov3_wsm/model_data/voc_classes.txt',
                             "anchors_path": self.realpath + '/yolov3_wsm/model_data/yolo_anchors.txt',
                             "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]], "input_shape": [416, 416],
                             "confidence": 0.5, "nms_iou": 0.3, "letterbox_image": False, "cuda": True}
        self.temp_path = "./result.jpg"
        self.imagePath = ""
        self.detect_mode = "yolov3"

        Form.setObjectName("Form")
        Form.resize(1280, 720)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_9.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 600))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_image = QtWidgets.QLabel(self.groupBox_2)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("./source/icon/3D.png"))
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.label_image.setMinimumSize(750,600)
        self.label_image.setMaximumSize(1500,1200)
        self.verticalLayout_4.addWidget(self.label_image)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QtCore.QSize(380, 1080))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_7.setMaximumSize(QtCore.QSize(360, 350))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(QtGui.QFont("Roman times", 12, QtGui.QFont.Bold))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.horizontalLayout_11.addWidget(self.label_2)
        self.comboBox_mode = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setFont(font)
        self.horizontalLayout_11.addWidget(self.comboBox_mode)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.radioButton_showImages = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_showImages.setChecked(True)
        self.radioButton_showImages.setObjectName("radioButton_showImages")
        self.radioButton_showImages.setFont(font)
        self.verticalLayout.addWidget(self.radioButton_showImages)
        self.radioButton_tipShowImages = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_tipShowImages.setObjectName("radioButton_tipShowImages")
        self.radioButton_tipShowImages.setFont(font)
        self.verticalLayout.addWidget(self.radioButton_tipShowImages)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_3.setMaximumSize(QtCore.QSize(150, 120))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(font)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("微软雅黑"))
        self.horizontalLayout_6.addWidget(self.label)
        self.button_imagePath = QtWidgets.QPushButton(self.groupBox_3)
        self.button_imagePath.setMaximumSize(QtCore.QSize(120, 16777215))
        self.button_imagePath.setFont(QtGui.QFont("微软雅黑"))
        self.button_imagePath.setStyleSheet("background-color: rgb(215, 255, 249);")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./source/icon/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.button_imagePath.setIcon(icon)
        self.button_imagePath.setCheckable(False)
        self.button_imagePath.setAutoRepeat(False)
        self.button_imagePath.setAutoExclusive(False)
        self.button_imagePath.setObjectName("button_imagePath")
        self.horizontalLayout_6.addWidget(self.button_imagePath)
        self.horizontalLayout_9.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_4.setMaximumSize(QtCore.QSize(150, 120))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setFont(font)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 150))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(QtGui.QFont("微软雅黑"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.button_imagePath_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.button_imagePath_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.button_imagePath_2.setFont(QtGui.QFont("微软雅黑"))
        self.button_imagePath_2.setStyleSheet("background-color: rgb(215, 255, 249);")
        # self.button_imagePath_2.setIcon(icon)
        self.button_imagePath_2.setObjectName("button_imagePath_2")
        self.horizontalLayout_8.addWidget(self.button_imagePath_2)
        self.horizontalLayout_9.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_detection = QtWidgets.QPushButton(self.groupBox_7)
        self.button_detection.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_detection.setObjectName("button_detection")
        self.button_detection.setFont(font)
        self.horizontalLayout.addWidget(self.button_detection)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setMaximumSize(QtCore.QSize(360, 200))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setFont(QtGui.QFont("Roman times",12,QtGui.QFont.Bold))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.label_result = QtWidgets.QLabel(self.groupBox_5)
        self.label_result.setMinimumSize(QtCore.QSize(0, 300))
        self.label_result.setMaximumSize(QtCore.QSize(16777215, 300))
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        self.label_result.setFont(QtGui.QFont("微软雅黑",10,QtGui.QFont.Bold))
        self.verticalLayout_6.addWidget(self.label_result)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.imageDetect = imageDetectionThread.ImageDetectionThread()
        self.imageDetect.infoEmit.connect(self._infoEmitEvent)
        self.imageDetect.overEmit.connect(self.killRealTimeDetectionThread)
        self.button_imagePath.clicked.connect(self.imageRead)
        self.button_imagePath_2.clicked.connect(self.modelRead)
        self.button_detection.clicked.connect(self.imageDetection)
        self.comboBox_mode.currentIndexChanged.connect(self.detectMode)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "安全检测系统"))
        self.label_3.setText(_translate("Form", "X光图像检测"))
        self.label_2.setText(_translate("Form", "识别算法："))
        self.comboBox_mode.setItemText(0, _translate("Form", "YoloV3_wsm"))
        self.comboBox_mode.setItemText(1, _translate("Form", "CenterNet"))
        self.comboBox_mode.setItemText(2, _translate("Form", "YoloV4"))
        self.radioButton_showImages.setText(_translate("Form", "图像窗体内显示"))
        self.radioButton_tipShowImages.setText(_translate("Form", "图像弹出窗展示"))
        self.groupBox_3.setTitle(_translate("Form", "单张图像识别"))
        self.label.setText(_translate("Form", "图像路径"))
        self.button_imagePath.setText(_translate("Form", "选择路径"))
        self.groupBox_4.setTitle(_translate("Form", "识别模型选取"))
        self.label_6.setText(_translate("Form", "模型路径"))
        self.button_imagePath_2.setText(_translate("Form", "选择路径"))
        self.button_detection.setText(_translate("Form", "违禁品检测"))
        self.groupBox_5.setTitle(_translate("Form", "识别目标"))

    def _infoEmitEvent(self, type, infoStr):
        """
        顶层信号槽函数
        :param type: I-信息
        :param infoStr:
        :return:
        """
        self.infoEmit.emit(type, infoStr)
        if type == "A":
            if infoStr != "null":
                labels = infoStr.split(",")
                result = {}
                for label in labels:
                    if label in result.keys():
                        result[label] += 1
                    else:
                        result[label] = 1
                s = ""
                for key in result.keys():
                    s += '\t'
                    s += key
                    s += '\t'
                    s += str(result[key])
                    s += '\n'
                self.label_result.setText(s)
            else:
                self.label_result.setText("")
            if self.radioButton_showImages.isChecked():
                self._setLabelPixmap(self.temp_path)
            else:
                image = Image.open(self.temp_path)
                image.show()

    def detectMode(self):
        mode = self.comboBox_mode.currentText()
        if mode == "CenterNet":
            self.detect_mode = "centernet"
            self._default = {"model_path": self.realpath + '/logs/ep071-loss1.658-val_loss1.688.pth',
                             "classes_path": self.realpath + '/centernet/model_data/voc_classes_ch.txt',
                             "backbone": 'resnet50', "input_shape": [512, 512],
                             "confidence": 0.3, "nms_iou": 0.3, "nms": True, "letterbox_image": False, "cuda": True}
        elif mode == "YoloV4":
            self.detect_mode = "yolov4"
            self._default = {"model_path": self.realpath + '/logs/ep043-loss1.984-val_loss1.405.pth',
                             "classes_path": self.realpath + '/yolov4/model_data/voc_classes.txt',
                             "anchors_path": self.realpath + '/yolov4/model_data/yolo_anchors.txt',
                             "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]], "input_shape": [416, 416],
                             "confidence": 0.3, "nms_iou": 0.3, "nms": True, "letterbox_image": False, "cuda": True}
        elif mode == "YoloV3_wsm":
            self.detect_mode = "yolov3"
            self._default = {"model_path": self.realpath + '/logs/ep100-loss4.459-val_loss3.782.pth',
                             "classes_path": self.realpath + '/yolov3_wsm/model_data/voc_classes.txt',
                             "anchors_path": self.realpath + '/yolov3_wsm/model_data/yolo_anchors.txt',
                             "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]], "input_shape": [416, 416],
                             "confidence": 0.5, "nms_iou": 0.3, "letterbox_image": False, "cuda": True}
        print(self.detect_mode)

    def imageRead(self):
        filePath, type = QtWidgets.QFileDialog.getOpenFileName(self.parent(), "导入图像", "\VOCdevkit\VOC2007\JPEGImages",
                                                               "JPEG(*JPG);;PNG(*PNG);;TIFF(*.TIF);;All Files (*)")
        if filePath != "":
            print(filePath)
            self.imagePath = filePath
            self._setLabelPixmap(filePath)
            self.label_result.setText("")
        else:
            self._infoEmitEvent("I", "提示：已取消导入图像")
            return

    def _setLabelPixmap(self, image, location=None):
        """
        图像显示到界面
        :param image: Image类型图像
        :return:
        """
        self.label_image.setPixmap(QtGui.QPixmap(""))
        if location is None:
            self.label_image.setPixmap(
                QtGui.QPixmap(QtGui.QPixmap(image).scaled(self.label_image.width(), self.label_image.height())))
        else:
            self.label_image.setPixmap(
                QtGui.QPixmap(QtGui.QPixmap(image).scaled(self.label_fig.width(), self.label_fig.height())))

    def modelRead(self):
        filePath, type = QtWidgets.QFileDialog.getOpenFileName(self.parent(), "导入模型", "\logs",
                                                               "PTH(*PTH);;All Files (*)")
        if filePath != "":
            self._default["model_path"] = filePath
            print(self._default)
        else:
            self._infoEmitEvent("I", "提示：已取消导入模型")
            return

    def imageDetection(self):
        if not self.imagePath:
            self._infoEmitEvent("I", "提示：未选择图片")
            return
        self.startImagesDectThread()

        # image, labels = predict.predict_image(self.imagePath, self._default)
        # image.save(self.temp_path)
        # if labels:
        #     labels = labels.split(",")
        #     del labels[-1]
        #     result = {}
        #     for label in labels:
        #         if label in result.keys():
        #             result[label] += 1
        #         else:
        #             result[label] = 1
        #     print(result)
        #     s = ""
        #     for key in result.keys():
        #         s += '\t'
        #         s += key
        #         s += '\t'
        #         s += str(result[key])
        #         s += '\n'
        #     self.label_result.setText(s)
        # else:
        #     self.label_result.setText("")
        # if self.radioButton_showImages.isChecked():
        #     self._setLabelPixmap(self.temp_path)
        # else:
        #     image.show()


    def startImagesDectThread(self):
        self.imageDetect.setPara(self.imagePath,self.detect_mode,self._default)
        self._infoEmitEvent("T","开启线程！")
        self.imageDetect.start()
        self._infoEmitEvent("T","线程已经开启,加载模型中.......")

    def killRealTimeDetectionThread(self):
        self.imageDetect.killThread()
        print("子线程关闭")
        self._infoEmitEvent("T", " - 子线程关闭.\n")