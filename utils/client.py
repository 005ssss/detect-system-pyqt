import socket
import threading
import time
import struct
import os

class Client():
    def __init__(self, ip, port, time_delay):
        self.ip = ip
        self.port = port
        self.delay = time_delay
        self.started = False
        self.realpath = os.path.realpath(r".")
        self.realpath = self.realpath.split("\\")
        self.realpath = "/".join(self.realpath) + "/download/"
        self.imagelist = os.listdir(self.realpath)  # 获取待检测图片文件夹中的全部文件列表
        self.threadLock = threading.Lock()
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.longLinkStart()

    def longLinkStart(self):
        server_address = (self.ip, int(self.port))
        self.socket_client.connect(server_address)
        tlonglink = threading.Thread(target=self.recvmsg)
        tlonglink.start()

    def sendfile(self):
        cnt = 0
        while cnt < 100:
            if not self.started:
                self.t.join()
                raise ValueError("stopped")
            print(cnt)
            with open(self.realpath + self.imagelist[0], "rb") as f:
                image = f.read()
            del self.imagelist[0]
            cnt += 1
            message = b"\xea\x31"
            message += struct.pack("b", cnt)
            message += struct.pack("i", len(image)+15)
            message += struct.pack(">ibb", 65535, 1, 1)
            message += struct.pack("b", 1)
            message += image
            message += b"\x03"
            self.socket_client.send(message)

            time.sleep(self.delay)

        return

    def recvmsg(self):
        while True:
            print("start")
            re = self.socket_client.recv(4)
            print(re)
            if len(re) > 0:
                cmd = re[1]
                self.socket_client.send(re)
                if cmd == 50:
                    self.started = True
                    self.t = threading.Thread(target=self.sendfile)
                    self.t.start()
                elif cmd == 52:
                    self.started = False


if __name__ == '__main__':
    client = Client("192.168.0.101", 45555, 0.5)