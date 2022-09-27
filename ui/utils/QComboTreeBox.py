from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QListView, QTreeView, QApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QMouseEvent
from PyQt5.Qt import Qt, QRect
from collections import deque
import sys


class QComboTreeBox(QComboBox):
    class MyTreeView(QTreeView):
        def __init__(self, parent: QWidget = None, vars=None):
            super().__init__(parent)
            self.vars = vars
            self.setExpandsOnDoubleClick(False)
            self.setHeaderHidden(True)

        def mousePressEvent(self, event):
            self.vars["lock"] = False
            currIndex = self.currentIndex()
            index = currIndex.sibling(currIndex.row(), 0).data()  # 获取同一行不同列的数据
            self.vars["currIndex"] = currIndex

            '''自己创建点击节点Node三角折叠/展开功能'''
            rect = self.visualRect(currIndex)
            expandOrCollape = QRect(rect.left() - 20, rect.top(), 20, rect.height())
            if expandOrCollape.contains(event.pos()):
                self.vars["expandOrCollape"] = True
                if self.isExpanded(currIndex):
                    self.setExpanded(currIndex, False)
                else:
                    self.setExpanded(currIndex, True)
            else:
                self.vars["expandOrCollape"] = False
            '''自己创建点击节点Node三角折叠/展开功能'''

            # super().mousePressEvent(event)   # super()会出现节点打不开的情况，所以才自己创建点击节点Node三角折叠/展开功能

        def mouseDoubleClickEvent(self, event):
            self.vars["lock"] = False
            super().mouseDoubleClickEvent(event)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vars = dict()
        self.item = ['枪', '刀', '钳子', '扳手', '剪刀']
        self.vars["lock"] = True
        self.vars["lineEdit"] = QLineEdit(self)
        self.vars["lineEdit"].setReadOnly(True)
        self.vars["listView"] = self.MyTreeView(self, self.vars)
        self.vars["listViewModel"] = QStandardItemModel(self)
        self.setModel(self.vars["listViewModel"])
        self.setView(self.vars["listView"])
        self.setLineEdit(self.vars["lineEdit"])
        self.vars["data_length"] = None
        self.view_settings()
        self.activated.connect(self.__show_selected)
        # self.add_item("(全选)")
        # self.add_item("其他")
        data = [(1, 0, '枪'), (2, 0, '刀'), (3, 0, '钳子'), (4, 0, '扳手'), (5, 0, '剪刀')]
        self.importData(data)

    # QtreeView展示视图的一些设置
    def view_settings(self):
        self.view().setMinimumWidth(150)
        self.view().setMinimumHeight(150)
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    # 往QtreeView中添加数据
    def importData(self, data, root=None):
        self.vars["listViewModel"].setRowCount(0)
        if root is None:
            root = QStandardItem()
            self.vars["listViewModel"].appendRow(root)
            root.setText("有违禁品")
            root.setCheckable(True)
            root.setCheckState(Qt.Checked)
        seen = {}  # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value[1] == 0:
                parent = root
            else:
                pid = value[1]
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value[0]
            child = QStandardItem()
            child.setText(value[2])
            child.setCheckable(True)
            child.setCheckState(Qt.Checked)
            parent.appendRow([
                child,
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)
        self.vars["data_length"] = len(data)

    # 展示下拉框
    def __show_selected(self, index):
        this = self.vars["currIndex"]
        model = self.vars["listViewModel"]
        current_standardItem = model.itemFromIndex(this)
        item = self.vars["listViewModel"].item(index)
        if self.vars["expandOrCollape"]:
            pass
            # print("Mouse_Clicked_On_ExpandOrCollape")
        else:
            current_standardItem.setCheckState(
                Qt.Unchecked if current_standardItem.checkState() == Qt.Checked else Qt.Checked)
            # 开始递归寻找子节点
            self.QcomboTreebox_child_node(current_standardItem)
            self.checkState_set(current_standardItem)
            self.Combobox_LineEdit_showText()
        self.vars["lock"] = True

    # 设置复选框状态
    def checkState_set(self, currItem):
        rootItem = self.vars["listViewModel"].item(0)
        currParent = currItem.parent()
        count = 0
        if currParent != None:
            currParent_childCount = currParent.rowCount()
            for i in range(currParent_childCount):
                if currParent.child(i).checkState() == Qt.Checked:
                    count += 1
            if currParent != rootItem:
                if count == currParent_childCount:
                    currParent.setCheckState(Qt.Checked)
                elif 0 < count < currParent_childCount:
                    currParent.setCheckState(Qt.PartiallyChecked)
                else:
                    currParent.setCheckState(Qt.Unchecked)
        l = len(self.get_selected())
        if currParent != None and 0 < l < self.vars["data_length"]:
            rootItem.setCheckState(Qt.PartiallyChecked)
        elif l == self.vars["data_length"]:
            rootItem.setCheckState(Qt.Checked)
        elif l == 0:
            rootItem.setCheckState(Qt.Unchecked)

    # 递归寻找所有子节点，并改变其复选框状态
    def QcomboTreebox_child_node(self, item):
        if item.hasChildren() == True:
            total_child_count = item.rowCount()
            for i in range(total_child_count):
                child_item = item.child(i)
                child_item.setCheckState(Qt.Checked if item.checkState() == Qt.Checked else Qt.Unchecked)
                self.QcomboTreebox_child_node(child_item)

    # 递归寻找所有父节点,并展开
    def QcomboTreebox_parent_node(self, item):
        if item.parent() != None:
            pitem = item.parent()
            pitem.setExpanded(True)
            self.QcomboTreebox_parent_node(pitem)

    # 获取当前选择的子项
    def get_selected(self):
        items = list()
        for row in range(0, self.vars["listViewModel"].rowCount()):
            item = self.vars["listViewModel"].item(row)
            self.get_child_item(item, items)
        return items

    # 用于get_selected函数的递归函数
    def get_child_item(self, item, items):
        if item.hasChildren() == True:
            total_child_count = item.rowCount()
            for i in range(total_child_count):
                child_item = item.child(i)
                if child_item.checkState() == Qt.Checked:
                    items.append(child_item.text())
                self.get_child_item(child_item, items)

    # 清空所有子项
    def clear_items(self):
        self.vars["listViewModel"].clear()

    # 检测下拉框是否已有数据
    def is_already_hasdata(self):
        return True if self.vars["listViewModel"].rowCount() != 0 else False

    # 下拉框LineEdit展示文本
    def Combobox_LineEdit_showText(self):
        items = self.get_selected()
        self.item = items
        l = len(items)
        is_all = bool(self.vars["listViewModel"].item(0).checkState() == Qt.Checked)
        self.vars["lineEdit"].setText(
            "有违禁品" if is_all == True else "(无选择)" if l == 0 else ";".join((item for item in items)))

    # 重写下拉框收起事件条件
    def hidePopup(self):
        if self.vars["lock"]:
            super().hidePopup()


def run():
    app = QApplication(sys.argv)
    win = QComboTreeBox()
    def pri():
        print(win.item)
    win.activated.connect(pri)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()