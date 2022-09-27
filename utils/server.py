import socket
import struct
from multiprocessing import Process
import time
from datetime import datetime

class Server():
    def __init__(self, port, time_delay):
        self.port = port
        self.delay = time_delay
        self.databuf = b''
        self.datalength = 0
        self.index = 1

        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind(("", self.port))
        self.socket_server.listen(128)
        self.client, self.addr = self.socket_server.accept()
        print(self.client)
        print('Connection from %s' % str(self.addr[0]))

    def datadownload(self):
        while True:
            try:
                buf = self.client.recv(2048)
                if len(buf) > 0:
                    self.databuf += buf
                    if self.dealData():
                        print("Sendfile stopped")
                        return
                else:
                    return

            except OSError as e:
                time.sleep(3)


    def dealData(self):
        length = len(self.databuf)
        if 0 < self.datalength <= length:
            filename = "image_%s_%s.jpg" % (datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M_%S'), self.index)
            with open("download/"+filename, "wb") as f:
                f.write(self.databuf[14:self.datalength-1])
            print(filename+" Downloaded")
            self.databuf = self.databuf[self.datalength:]
            self.datalength = 0
        else:
            cmd = self.databuf[1]
            if cmd == 49:
                self.index = self.databuf[2]
                self.datalength = struct.unpack("i",self.databuf[3:7])[0]
            elif cmd == 52:
                return True
        return False

    def startup(self):
        message = b"\xea\x32"
        message += struct.pack("b", self.index)
        message += b"\x03"
        self.client.send(message)
        print(message)
        rec = self.client.recv(2048)
        if rec == message:
            # 创建新线程来处理TCP连接:
            self.t = Process(target=self.datadownload)
            self.t.start()
        else:
            self.startup()

    def startreverse(self):
        message = b"\xea\x33"
        message += struct.pack("b", self.index)
        message += b"\x03"
        self.client.send(message)
        rec = self.client.recv(2048)
        if rec == message:
            # 创建新线程来处理TCP连接:
            t = threading.Thread(target=self.datadownload)
            t.start()
        else:
            self.startup()

    def stop(self):
        message = b"\xea\x34"
        message += struct.pack("b", self.index)
        message += b"\x03"
        self.client.send(message)
        rec = self.client.recv(2048)
        self.t.join()
        if rec != message:
            self.stop()


if __name__ == '__main__':
    server = Server(45555,1)
    server.startup()
    time.sleep(5)
    print(server.databuf)
    server.stop()
    server.startup()
