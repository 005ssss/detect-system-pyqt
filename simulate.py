import base64
import os
import time
from ui.utils.SingleModel import centernetModel, predict_image

import MySQLdb
import requests

file_dir = "C:/Users/HP/Desktop/package/"

file_name = os.listdir(file_dir)

result_path = "C:/Users/HP/Desktop/detect-system-main/results.jpg"

i = 0

while i < len(file_name):
    db = MySQLdb.connect(host='192.168.56.10', user='root', password='991010', db='logistics_package')
    cur = db.cursor()
    cur.execute("select state from serv_state where id = %d" %1001)
    state = cur.fetchall()[0][0]
    db.close()
    if(state):
        image, labels, boxes = predict_image(file_dir + file_name[i], centernetModel)
        # 空数组无法发送请求
        if labels == []:
            labels = [""]
        if boxes == []:
            boxes = [""]
        image.save(result_path)
        with open(result_path, 'rb') as f:
            img = base64.b64encode(f.read()).decode()
        image = []
        image.append(img)
        res = {"name": file_name[i], "image": image, "labels": labels, "boxes": boxes}
        # 访问服务
        _ = requests.post("http://localhost:9001/pkg/detect/centernet", data=res)
        i += 1
        time.sleep(0.35)
    else:
        time.sleep(0.5)
