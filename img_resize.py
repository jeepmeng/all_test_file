import os

import cv2
import numpy as np




# 双线性插值放大、缩小reshape图片---opencv---参数：输入文件，输出文件，放大或缩小倍数（建议：0-10）
def image_resize(input,output,num):
    img = cv2.imread(input, 1)
    src_h, src_w, channel = img.shape
    dst_h, dst_w = int(src_h*num), int(src_w*num)
    print("src_h, src_w = ", src_h, src_w)
    print("dst_h, dst_w = ", dst_h, dst_w)
    if src_h == dst_h and src_w == dst_w:
        return img.copy()
    # dst_h,dst_w = int(dst_h),int(dst_w)
    dst = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
    scale_x, scale_y = float(src_w) / dst_w, float(src_h) / dst_h  # 原图除以目标图
    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
                # 使得中心点重合
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5
                # 找到将用于计算插值的点的坐标，计算四个点来查找
                src_x0 = int(np.floor(src_x))  # np.floor---向下取整
                src_x1 = min(src_x0 + 1, src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)

                # calculate the interpolation
                temp0 = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[
                    src_y0, src_x1, i]
                temp1 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[
                    src_y1, src_x1, i]
                dst[dst_y, dst_x, i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
    if str(input).endswith("jpg"):
        cv2.imwrite(str(output).replace(".jpg","_resize_"+str(num)+".jpg"), dst)
    elif str(input).endswith("png"):
        cv2.imwrite(str(output).replace(".png","_resize_"+str(num)+".png"), dst)
    # return dst



def cv2_resize(ori_pth,obj_pth,num):
    file_list = os.listdir(ori_pth)
    if not os.path.exists(obj_pth):
        os.makedirs(obj_pth)


    for i in file_list:
        if i == '.DS_Store':
            continue
        cur_file = os.path.join(ori_pth,i)
        cur_list = os.listdir(cur_file)
        obj_img_file_pth = os.path.join(obj_pth, i)
        if not os.path.exists(obj_img_file_pth):
            os.makedirs(obj_img_file_pth)
        for k in cur_list:
            if k == '.DS_Store':
                continue

            ori_img_file = os.path.join(cur_file,k)

            obj_img_file = os.path.join(obj_img_file_pth, k)





            img = cv2.imread(ori_img_file)
            w,h,_ = img.shape

            for j in num:
                out = cv2.resize(img, (int(h*j),int(w*j)), interpolation=cv2.INTER_AREA)
                if str(obj_img_file).endswith("jpg"):
                    cv2.imwrite(str(obj_img_file).replace(".jpg","_resize_"+str(j).replace('.','')+".jpg"), out)
                    print('{}---is done!'.format(str(obj_img_file).replace(".jpg","_resize_"+str(j).replace('.','')+".jpg")))
                elif str(obj_img_file).endswith("png"):
                    cv2.imwrite(str(obj_img_file).replace(".png", "_resize_" + str(j).replace('.','') + ".png"), out)
                    print('{}---is done!'.format(
                        str(obj_img_file).replace(".png", "_resize_" + str(j).replace('.', '') + ".png")))


if __name__ == '__main__':
    ori_pth = '/Users/liufucong/Downloads/108'
    obj_pth = '/Users/liufucong/Downloads/108_resize'
    num = [0.15,0.2,0.25,0.3]

    cv2_resize(ori_pth,obj_pth,num)
    # obj_pth = '/newdata/fucongliu/out_temp_yancao_imgfile_new_resize'

