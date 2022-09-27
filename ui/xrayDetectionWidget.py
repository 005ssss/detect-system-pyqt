# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagesDetectionWight.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image
from ui.uiThreads import imagesDetectionThread, localDetectionThread
import socket
import struct
from ui.utils.SingleModel import centernetModel, yoloModel, yolo_wsm

class Ui_Form(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str, str)
    def setupUi(self, Form):
        #TCP/IP长链接
        self.port = 45555   #端口号
        self.index = 1
        self.isConnected = False
        self.model = yolo_wsm

        #获取文件夹路径
        self.realpath = os.path.realpath(r".")
        self.realpath = self.realpath.split("\\")
        self.realpath = "/".join(self.realpath)
        self.temp_path = "./results.jpg"
        self.imagePath = ""
        self.imagelist = os.listdir(self.realpath + '/VOCdevkit/VOC2007/JPEGImages')
        self.image_index = 0
        self.detect_mode = "yolov3_wsm"
        self.is_Pause = True    #开始/停止状态

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
        font.setFamily("宋体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
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
        self.label_3.setFont(QtGui.QFont("Roman times", 15, QtGui.QFont.Bold))
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
        self.label_2.setFont(QtGui.QFont("微软雅黑", 10))
        self.horizontalLayout_11.addWidget(self.label_2)
        self.comboBox_mode = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.setFont(QtGui.QFont("微软雅黑", 10))
        self.horizontalLayout_11.addWidget(self.comboBox_mode)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.radioButton_showImages = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_showImages.setChecked(True)
        self.radioButton_showImages.setObjectName("radioButton_showImages")
        self.radioButton_showImages.setFont(QtGui.QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.radioButton_showImages)
        self.radioButton_tipShowImages = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_tipShowImages.setObjectName("radioButton_tipShowImages")
        self.radioButton_tipShowImages.setFont(QtGui.QFont("微软雅黑", 10))
        self.verticalLayout.addWidget(self.radioButton_tipShowImages)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_detection = QtWidgets.QPushButton(self.groupBox_7)
        self.button_detection.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_detection.setObjectName("button_detection")
        self.button_detection.setFont(QtGui.QFont("微软雅黑", 10))
        self.button_detection.setStyleSheet("QPushButton{background-color:#F0F8FF }")
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

        self.imageDetect = imagesDetectionThread.ImagesDetectionThread()
        self.imageDetect.infoEmit.connect(self._infoEmitEvent)
        # self.imageDetect.overEmit.connect(self.killRealTimeDetectionThread)
        self.localDetect = localDetectionThread.LocalDetectionThread()
        self.localDetect.infoEmit.connect(self._infoEmitEvent)
        self.localDetect.overEmit.connect(self.killLocalDetectionThread)
        self.button_detection.clicked.connect(self.detectButton)
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
        self.button_detection.setText(_translate("Form", "违禁品检测"))
        self.groupBox_5.setTitle(_translate("Form", "识别目标"))

    #tcp连接
    def tcpConnect(self):
        if self.is_Pause:
            self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_server.bind(("", self.port))
            self.socket_server.listen(128)
            self.client, self.addr = self.socket_server.accept()    #开启连接监听，等待客户端连接
            print('Connection from %s' % str(self.addr[0]))
            self.isConnected = True
            self._infoEmitEvent("I", "成功链接到设备")

    def _infoEmitEvent(self, type, infoStr):
        """
        顶层信号槽函数
        :param type: I-信息
        :param infoStr:
        :return:
        """
        self.infoEmit.emit(type, infoStr)
        if type == "A":
            if infoStr != "":
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
            self.model = centernetModel
        elif mode == "YoloV4":
            self.detect_mode = "yolov4"
            self.model = yoloModel
        else:
            self.detect_mode = "yolov3_wsm"
            self.model = yolo_wsm

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

    #启动/停止按钮
    def detectButton(self):
        if not self.isConnected:
            if self.is_Pause:
                self.is_Pause = False
                self.button_detection.setText("停止检测")
                self.imageDetection()
            else:
                self.is_Pause = True
                self.button_detection.setText("违禁品检测")
        else:
            if self.is_Pause:
                self.is_Pause = False
                self.button_detection.setText("停止检测")
                self.startup()
            else:
                self.is_Pause = True
                self.button_detection.setText("违禁品检测")
                self.stop()

    def imageDetection(self):
        if len(self.imagelist) == 0 or self.is_Pause:
            return
        rootPath = self.realpath + "/VOCdevkit/VOC2007/JPEGImages/"
        self.imagePath = rootPath + self.imagelist[0]
        del self.imagelist[0]
        print(self.imagePath)
        self.startLocalDectThread()

    def startImagesDectThread(self):
        self.imageDetect.setPara(self.realpath, self.client, self.model)
        self._infoEmitEvent("TH","开启线程！")
        self.imageDetect.start()
        self._infoEmitEvent("TH","线程已经开启,加载模型中.......")

    def startLocalDectThread(self):
        self.localDetect.setPara(self.imagePath, self.model)
        self._infoEmitEvent("T", "开启线程！")
        self.localDetect.start()
        self._infoEmitEvent("T", "线程已经开启,加载模型中.......")

    def killLocalDetectionThread(self):
        self.localDetect.killThread()
        print("子线程关闭")
        self._infoEmitEvent("T", " - 子线程关闭.\n")
        self.imageDetection()

    #X光机开启指令
    def startup(self):
        message = b"\xeb\x32"
        message += struct.pack("b", self.index)
        message += b"\x03"
        print(message)
        self.client.send(message)
        rec = self.client.recv(4)
        print(rec)
        if len(rec) > 0:
            # 创建新线程来处理X光机传来的图片:
            self.startImagesDectThread()
        else:
            self.startup()

    #X光机反转指令
    def startreverse(self):
        message = b"\xeb\x33"
        message += struct.pack("b", self.index)
        message += b"\x03"
        self.client.send(message)
        rec = self.client.recv(4)
        print(rec)
        if len(rec) > 0 and rec[1] == 50:
            # 创建新线程来处理TCP连接:
            self.startImagesDectThread()
        else:
            self.startup()

    #X光机停止指令
    def stop(self):
        message = b"\xeb\x34"
        message += struct.pack("b", self.index)
        message += b"\x03"
        self.client.send(message)
        rec = self.client.recv(4)
        print(rec)
        # rec = self.client.recv(4)
        # if len(rec) == 0:
        #     self.stop()