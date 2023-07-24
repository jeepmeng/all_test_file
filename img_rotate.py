from PIL import Image
import os
import cv2
import numpy as np


pth = r'/Users/liufucong/Downloads/旋转图像'
img_file =os.listdir(pth)
print(img_file)

# for i in img_file[1:]:

# 读取图像
#     im = Image.open(os.path.join(pth,i))

img=cv2.imread(os.path.join(pth,img_file[1]))
print(img.shape)

# img90=np.rot90(img)
cv2.imshow('hhh',img)
cv2.waitKey()
# 指定逆时针旋转的角度
#     im_rotate = im.rotate(45)
#     im_save = im_rotate.save(os.path.join(pth,i))
#     cv2.imwrite(os.path.join(pth,i),img90)