from ui.utils.SingleModel import predict_image
from PyQt5.QtCore import pyqtSignal, QThread
import MySQLdb
import time
from ui.utils.sqlCreate import sqlCreate


class LocalDetectionThread(QThread):
    infoEmit = pyqtSignal(str, str)
    overEmit = pyqtSignal()

    def __init__(self):
        super(LocalDetectionThread, self).__init__()

    def setPara(self, *args):
        self.imagePath = args[0]
        self.model = args[1]
        self.temp_path = "./results.jpg"

    def run(self) -> None:
        self._sendInfo("T", "子线程已开启....")
        print("子线程已开启....")
        # try:
        #     # 预启动模型
        image = 0
        labels = []
        self.db = sqlCreate().createSql()
        self.cur = self.db.cursor()

        image, labels, boxes = predict_image(self.imagePath, self.model)
        image.save(self.temp_path)
        isNull = 1
        if labels == []:
            labels = ""
            boxes = 0
            isNull = 0
        else:
            boxes = ''.join(str(i) + ',' for i in boxes)
        sql = ''' insert into check_data values(%s, '%s', '%s', %s, %s, '%s')''' % (
            0, self.imagePath, labels, isNull, "NOW()", boxes)
        self.cur.execute(sql)
        self.db.commit()
        self.db.close()
        self._sendInfo("A", labels)
        time.sleep(0.5)     # 休眠0.5s
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