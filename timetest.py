from ui.utils.SingleModel import centernetModel, predict_image
import time

path = 'C:/Users/HP/Desktop/detect-system-main/VOCdevkit/VOC2007/JPEGImages/P00042.jpg'
for i in range(0,8):
    print(time.time())
    predict_image(path, centernetModel)