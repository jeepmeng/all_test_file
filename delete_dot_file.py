import os

import shutil
import random


pth_1 = '/newdata/fucongliu/xxx------目标文件夹--去杂项--二次添加'

# pth_2 = '/home/xht/danhe_zq'
filenames_1 = os.listdir(pth_1)
print(len(filenames_1))

for i in filenames_1:
    if '.' in i.split('_') or '.DS' in i.split('_'):
        print(i)



        enumerate