# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ui.utils import sliderButton
import sys


class setDialog(QtWidgets.QWidget):
    infoEmit = QtCore.pyqtSignal(str, str)
    def __init__(self, style_color,parent=None):
        super(setDialog, self).__init__(parent)
        self.setObjectName("Dialog")
        self.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_5)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.comboBox.setCurrentIndex(style_color)
        self.comboBox.currentIndexChanged.connect(self.changeStyle)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "界面设置"))
        self.groupBox.setTitle(_translate("Dialog", "基本设置"))
        self.label.setText(_translate("Dialog", "中文标题"))
        self.lineEdit.setText(_translate("Dialog", "安全检测系统"))
        self.label_2.setText(_translate("Dialog", "界面样式"))
        self.comboBox.setItemText(0, _translate("Dialog", "深蓝色"))
        self.comboBox.setItemText(1, _translate("Dialog", "浅蓝色"))
        self.comboBox.setItemText(2, _translate("Dialog", "灰色"))
        self.label_4.setText(_translate("Dialog", "英文标题"))
        self.lineEdit_2.setText(_translate("Dialog", "Security Detection System"))

    def changeStyle(self):
        self.infoEmit.emit("T", str(self.comboBox.currentIndex()))

class My_Main_Window(QtWidgets.QMainWindow):
    '''主程序'''
    def __init__(self):
        super(My_Main_Window, self).__init__()
        self.setupUi(self)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.button)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 新建窗口
    MainWindow = setDialog()
    MainWindow.show()
    app.exit(app.exec_())