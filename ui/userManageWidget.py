# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\userManageWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb
import sys
from ui.utils import sqlCreate

class Ui_Form(QtCore.QObject):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 662)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setStyleSheet("QPushButton{background-color:#F0F8FF }")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 550))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 1080))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)    #设置表格不可编辑
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #设置表格不可编辑
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.icon1 = QtGui.QIcon()
        self.icon1.addPixmap(QtGui.QPixmap("./source/icon/bianji.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap("./source/icon/shanchu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.getTable()
        self.pushButton.clicked.connect(self.createUser)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "新建用户"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "密码"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "操作"))

    def getTable(self):
        db = MySQLdb.connect(host='localhost', user='root', password='991010', db='test')
        cur = db.cursor()

        sql = '''select * from users'''
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        table = self.tableWidget
        table.setRowCount(0)
        if not data:
            return
        for i in range(len(data)):
            table.insertRow(i)
            for j in range(len(data[0])):
                temp = QtWidgets.QTableWidgetItem(str(data[i][j]))
                temp.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(i, j, temp)
            table.setCellWidget(i, len(data[0]), self.buttonForRow())

    def buttonForRow(self):
        widget = QtWidgets.QWidget()
        # 修改
        self.updateBtn = QtWidgets.QPushButton()
        self.updateBtn.setIcon(self.icon1)
        self.updateBtn.setIconSize(QtCore.QSize(30, 30))
        self.updateBtn.setMaximumWidth(30)
        self.updateBtn.clicked.connect(self.UpdateButton)

        # 删除
        self.deleteBtn = QtWidgets.QPushButton()
        self.deleteBtn.setIcon(self.icon2)
        self.deleteBtn.setIconSize(QtCore.QSize(30, 30))
        self.deleteBtn.setMaximumWidth(30)
        self.deleteBtn.clicked.connect(self.DeleteButton)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def UpdateButton(self):
        button = self.tableWidget.sender()
        if button:
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            self.dialog = editDialog("E", self.tableWidget.item(row, 1).text())
            self.dialog.show()
            self.dialog.my_Signal.connect(self.getTable)

    def DeleteButton(self):
        button = self.tableWidget.sender()
        if button:
            row = self.tableWidget.indexAt(button.parent().pos()).row()
            reply = QtWidgets.QMessageBox.question(self.parent(), '用户管理', '确定要删除该用户吗？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                id = self.tableWidget.item(row, 0).text()
                db = sqlCreate.sqlCreate().createSql()
                cur = db.cursor()
                sql = '''delete from users where user_id = %s''' % (id)

                cur.execute(sql)
                db.commit()
                db.close()
                self.getTable()


    def createUser(self):
        self.dialog = editDialog("N")
        self.dialog.show()
        self.dialog.my_Signal.connect(self.getTable)


class editDialog(QtWidgets.QWidget):
    my_Signal = QtCore.pyqtSignal(str)
    def __init__(self, type, id=None, parent=None):
        super(editDialog, self).__init__(parent)
        self.type = type
        self.id = id

        self.setWindowTitle("编辑用户信息")
        self.setObjectName("Dialog")
        self.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/icon/comment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("确认密码：")
        self.label_2.setFont(font)
        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("密      码：")
        self.label_3.setFont(font)
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("姓      名：")
        self.label_8.setFont(font)
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("用 户 名：")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        if self.type == "N":
            self.lineEdit = QtWidgets.QLineEdit(self)
        else:
            self.lineEdit = QtWidgets.QLabel(self.id)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.gridLayout.addWidget(self.lineEdit_3, 5, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(font)
        self.gridLayout.addWidget(self.lineEdit_4, 7, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setMinimumSize(QtCore.QSize(0, 10))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setMinimumSize(QtCore.QSize(0, 10))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setMinimumSize(QtCore.QSize(0, 10))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_7.setText("")
        self.label_7.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setDefault(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setFont(font)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def getData(self):
        return self.lineEdit.text(), self.lineEdit_3.text()

    def accept(self):
        if not self.lineEdit.text():
            QtWidgets.QMessageBox.information(self, '提示', '请输入用户名！')
        elif not self.lineEdit_2.text():
            QtWidgets.QMessageBox.information(self, '提示', '请输入姓名！')
        elif not self.lineEdit_3.text():
            QtWidgets.QMessageBox.information(self, '提示', '请输入密码！')
        elif self.lineEdit_3.text() != self.lineEdit_4.text():
            QtWidgets.QMessageBox.information(self, '提示', '请确认两次密码输入正确！')
        else:
            db = MySQLdb.connect(host='localhost', user='root', password='991010', db='test')
            cur = db.cursor()

            #编辑用户信息
            if self.type == "E":
                sql = '''update users set password= '%s' where user_name = '%s' ''' % (self.lineEdit_2.text(), self.id)
            #创建新用户
            else:
                #判断用户名是否存在
                sql = '''select * from users where user_name = '%s' ''' % (self.lineEdit.text())
                cur.execute(sql)
                data = cur.fetchall()
                if data:
                    QtWidgets.QMessageBox.information(self, '提示', '该用户已存在！')
                    return

                sql = '''insert into users values(0, '%s', '%s', '%s')''' % (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
            cur.execute(sql)
            db.commit()
            db.close()
            self.close()


    def reject(self):
        self.close()
        if self.type == "E":
            QtWidgets.QMessageBox.information(self, '提示', '已取消修改用户信息！')
        elif self.type == "N":
            QtWidgets.QMessageBox.information(self, '提示', '已取消创建用户！')

    def closeEvent(self, event):
        self.my_Signal.emit("exit")

    # def getResults(self):
    #     if self.exec_() == QtWidgets.QDialog.Accepted:
    #         # get all values
    #         val = self.some_widget.some_function()
    #         val2 = self.some_widget2.some_another_function()
    #         return val1, val2, ...
    #     else:
    #         return None