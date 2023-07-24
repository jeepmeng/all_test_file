import os

import shutil
import random


pth_1 = '/Volumes/T7/yancao_imgfile_new_xht_zq'
mubiao = '/newdata/fucongliu'
val = "val_lr_0001_2.txt"
train = "train_lr_0001_2.txt"
# pth_2 = '/home/xht/danhe_zq'
filenames_1 = os.listdir(pth_1)
print(len(filenames_1))
k = 0
with open(os.path.join(mubiao,train),'w') as f_train, open(os.path.join(mubiao,val),'w') as f_val:
    for j,i in enumerate(filenames_1):
        # if '.' in i.split('_') :
        if '.DS' in i.split('_') or '.' in i.split('_'):
            k+=1
            continue

        pth_img = os.listdir(os.path.join(pth_1, i))
        rate = round(len(pth_img)*0.1)
        last_img = random.sample(pth_img,rate)

        # with open('/Volumes/T7/xxxxxxxxxxxx------目标文件夹-------train_list/val.txt','w') as f:
        for i_1 in last_img:
            if '.DS' in i_1.split('_') or '.' in i_1.split('_'):
                continue
            f_val.write(os.path.join(pth_1, i) + '/' + i_1 +','+str(j-k)+ '\n')


        different = list(set(pth_img).difference(set(last_img)))
        for i_2 in different:
            if '.DS' in i_2.split('_') or '.' in i_2.split('_'):
                continue
            f_train.write(os.path.join(pth_1, i) + '/' + i_2 +','+str(j-k)+ '\n')
