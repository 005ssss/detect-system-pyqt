from ui.utils.sqlCreate import sqlCreate
from PyQt5.QtCore import pyqtSignal, QThread
import struct
import time
from datetime import datetime
from ui.utils.SingleModel import predict_image


class ImagesDetectionThread(QThread):
    infoEmit = pyqtSignal(str, str)
    overEmit = pyqtSignal(int)

    def __init__(self):
        super(ImagesDetectionThread, self).__init__()

    def setPara(self, *args):
        self.realpath = args[0]
        self.client = args[1]
        self.model = args[2]
        self.temp_path = "./results.jpg"
        self.databuf = b''
        self.datalength = 0
        self.index = 1

    def run(self) -> None:
        #持续处理图片
        while True:
            try:
                buf = self.client.recv(2048)
                if len(buf) > 0:
                    self.databuf += buf
                    #
                    if self.dealData():
                        self.databuf = b""
                        continue
            except:
                print("exception")
                time.sleep(1)
        # 结束，发送终止信号
        time.sleep(0.5)
        self.overEmit.emit(0)
        print("Stopped")
        return

    #处理数据帧
    def dealData(self):
        length = len(self.databuf)
        #判断当前读取字符长度是否超过图片长度
        if 0 < self.datalength <= length:
            filename = "image_%s_%s.jpg" % (datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S'), self.index)
            self.imagePath = self.realpath + "/utils/download/" + filename
            with open(self.imagePath, "wb") as f:
                f.write(self.databuf[14:self.datalength - 1])
            print(filename + " Downloaded")
            self.detect()
            self.databuf = self.databuf[self.datalength:]
            self.datalength = 0
        else:
            #获取图片字节长度
            cmd = self.databuf[1]
            if cmd == 49:
                self.index = self.databuf[2]
                self.datalength = struct.unpack("i", self.databuf[3:7])[0]
            else:
                return True
        return False

    def detect(self):
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
