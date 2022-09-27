# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\searchDataWight.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import colorsys
import MySQLdb
# from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from ui.utils import QComboTreeBox
from ui.utils import sqlCreate


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 662)
        self.input_shape = [416, 416]
        self.translate = {'枪':'Gun', '刀':'Knife', '钳子':'Pliers', '扳手':'Wrench', '剪刀':'Scissors'}
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 600))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 1080))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setWeight(QtGui.QFont.Bold)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView{font-size:10}")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setFont(font)
        self.dateEdit.setFont(font)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setWeight(QtGui.QFont.Bold)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboCheck = QComboTreeBox.QComboTreeBox()
        self.comboCheck.setFont(font)
        self.comboCheck.vars["listView"].setFont(font)
        self.comboCheck.setObjectName("comboCheck")
        self.horizontalLayout_2.addWidget(self.comboCheck)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:#F0F8FF }")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.chartview = QChartView()
        # self.chartview.setMinimumSize(300,300)
        self.verticalLayout_2.addItem(spacerItem)
        # self.verticalLayout_2.addWidget(self.chartview)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 编辑searchDataWidget中的表格控件
        self.dateEdit.setDate(QtCore.QDate.currentDate())  # 设置日期选择为当天
        self.dateEdit.setMaximumDate(QtCore.QDate.currentDate())  # 设置最大日期为当天
        self.table = self.tableWidget
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置表格不可编辑
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.table.hideColumn(5)
        self.table.hideColumn(6)
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 200)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.table.horizontalHeader().setFont(font)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.doubleClicked.connect(self.getRow)  # 双击打开图片
        self.checkBox.clicked.connect(self.noProhibited)
        self.comboCheck.activated.connect(self.Prohibited)
        # self.checkBox_2.clicked.connect(self.Prohibited)

        self.pushButton.clicked.connect(self.getData)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "图片名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "检测结果"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "是否违禁品"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "检测时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "检测框"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "图片地址"))
        self.label_4.setText(_translate("Form", "查询日期："))
        self.label_5.setText(_translate("Form", "查询类别："))
        self.checkBox.setText(_translate("Form", "无违禁品"))
        self.radioButton_2.setText(_translate("Form", "检测图片"))
        self.radioButton.setText(_translate("Form", "原图片"))
        self.pushButton.setText(_translate("Form", "查询"))

    def get_selected(self):
        ret = []
        for i in range(len(self.items)):
            if self.box_list[i].isChecked():
                ret.append(self.box_list[i].text())
        print(ret)


    """
    点击表格中的图片进行显示
    """
    def getRow(self, index):
        row = index.row()
        imagepath = self.table.item(row, 6).text()
        image = Image.open(imagepath)
        if self.radioButton.isChecked() or self.table.item(row, 3).text() == '否':
            image.show()
        else:
            font = ImageFont.truetype(font='./centernet/model_data/simhei.ttf',
                                      size=np.floor(3e-2 * np.shape(image)[1] + 0.5).astype('int32'))
            thickness = max((np.shape(image)[0] + np.shape(image)[1]) // self.input_shape[0], 1)
            labels = self.table.item(row, 2).text()
            boxes = self.table.item(row, 5).text()
            labels = labels.split(',')
            boxes = boxes.split(',')
            classes = {}
            c = 0
            for i in labels:
                if i not in classes:
                    classes[i] = c
                    c += 1
            if c < 6:
                c = 6
            hsv_tuples = [(x / c, 1., 1.) for x in range(c)]
            colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
            colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), colors))
            num = len(labels)
            for i in range(num):
                top, left, bottom, right, score = boxes[5 * i : 5 * (i + 1)]
                top = int(top)
                left = int(left)
                bottom = int(bottom)
                right = int(right)
                score = float(score)
                label = '{} {:.2f}'.format(labels[i], score)
                draw = ImageDraw.Draw(image)
                label_size = draw.textsize(label, font)
                label = label.encode('utf-8')
                if top - label_size[1] >= 0:
                    text_origin = np.array([left, top - label_size[1]])
                else:
                    text_origin = np.array([left, top + 1])

                for j in range(thickness):
                    draw.rectangle([left + j, top + j, right - j, bottom - j], outline=colors[classes[labels[i]]])
                draw.rectangle([tuple(text_origin), tuple(text_origin + label_size)], fill=colors[classes[labels[i]]])
                draw.text(text_origin, str(label, 'UTF-8'), fill=(0, 0, 0), font=font)
                del draw
            image.show()

    def noProhibited(self):
        is_no_prohibited = self.checkBox.isChecked()
        if is_no_prohibited:
            for i in range(self.table.rowCount()):
                if self.table.item(i, 3).text() == '否':
                    self.table.showRow(i)
        else:
            for i in range(self.table.rowCount()):
                if self.table.item(i, 3).text() == '否':
                    self.table.hideRow(i)

    def Prohibited(self):
        item = self.comboCheck.item
        for i in range(self.table.rowCount()):
            if self.table.item(i, 3).text() == '否':
                continue
            flag = 0
            res = self.table.item(i, 2).text()
            #判断检测结果是否包含筛选目标
            for j in item:
                if j in res or self.translate[j] in res:
                    flag = 1
                    break
            if flag == 1:
                self.table.showRow(i)
            else:
                self.table.hideRow(i)


    """
    查询数据库更新表格
    """
    def getData(self):
        db = sqlCreate.sqlCreate().createSql()
        cur = db.cursor()

        time = self.dateEdit.date()
        y, m, d = time.year(), time.month(), time.day()
        sql = '''select * from check_data where year(check_time) = %s and month(check_time) = %s and day(check_time) = %s''' %(y, m, d)
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        table = self.table
        table.setRowCount(0)
        if not data:
            # self.chartview.setChart(QChart())
            return
        dic = {}
        for i in range(len(data)):
            table.insertRow(i)
            if data[i][2]:
                words = data[i][2].split(',')
                for word in words:
                    if word not in dic:
                        dic[word] = 1
                    else:
                        dic[word] += 1
            for j in range(len(data[0])):
                if j == 1:
                    path = data[i][j]
                    table.setItem(i, 6, QtWidgets.QTableWidgetItem(path))
                    path = path.split("/")
                    temp = QtWidgets.QTableWidgetItem(path[-1])
                elif j == 3:
                    if data[i][j] == 0:
                        temp = QtWidgets.QTableWidgetItem("否")
                    else:
                        temp = QtWidgets.QTableWidgetItem("是")
                else:
                    temp = QtWidgets.QTableWidgetItem(str(data[i][j]))
                temp.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(i, j, temp)
        self.noProhibited()
        self.Prohibited()
        # chart = QChart()
        # chart.setTitle("%s月%s日违禁品统计" % (m,d))
        # chart.setTitleBrush(QtGui.QColor(0, 0, 0))
        # legend = chart.legend()
        # legend.setVisible(False)
        # legend.setLabelColor(QtGui.QColor(0, 0, 0))
        # series = QBarSeries()
        # tempBar = QBarSet("")
        # tempBar.append(list(dic.values()))
        # series.append(tempBar)
        # chart.addSeries(series)
        # axisx = QBarCategoryAxis()
        # axisx.append(list(dic.keys()))
        # chart.addAxis(axisx, QtCore.Qt.AlignBottom)
        # axisy = QValueAxis()
        # axisy.applyNiceNumbers()
        # chart.addAxis(axisy, QtCore.Qt.AlignLeft)
        # series.attachAxis(axisy)
        # self.chartview.setChart(chart)