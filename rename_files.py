import os

path = '/Users/liufucong/Downloads/0704_hbl_train_data/select'

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

# n = 0
for n,i in enumerate(fileList):
    # 设置旧文件名（就是路径+文件名）
    img_pth = os.listdir(os.path.join(path,i))
    for img_name in img_pth:
        # print(img_name)
        img_old_n = os.path.join(os.path.join(path,i),img_name)
        img_new_n = os.path.join(os.path.join(path,i),(str(n)+'_'+img_name))
        os.rename(img_old_n, img_new_n)

    oldname = os.path.join(path,i)  # os.sep添加系统分隔符

    # 设置新文件名
    newname = os.path.join(path,str(n))

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    # n += 1