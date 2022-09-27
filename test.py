import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import testwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 新建窗口
    MainWindow = QMainWindow()
    ui = testwindow.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exit(app.exec_())

