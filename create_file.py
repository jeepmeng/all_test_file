import os

# pth = '/Volumes/T7/xxx------目标文件夹--去杂项--二次添加'
#
# new_pth = '/Volumes/T7/烟草抠图/yancao_imgfile'
#
# img_file = os.listdir(pth)
#
# for i in img_file:
#     if i == '.DS_Store':
#         continue
#     if not os.path.exists(os.path.join(new_pth,i)):
#         os.makedirs(os.path.join(new_pth,i))



pth = '/Volumes/T7/烟草抠图/yancao_imgfile_new'

img_file = os.listdir(pth)

with open('/Volumes/T7/烟草抠图/dict_2.txt', 'w') as f:

    i_1 = 0
    for num, filename in enumerate(img_file):
        if filename == '.DS_Store':
            continue

        f.write(filename+','+str(num)+'\n')
        i_1+=1

        # recent_filename = os.path.join(pth,filename)
        # new_name = os.path.join(pth,str(num))
        #
        # os.rename(recent_filename, new_name)
        # print(recent_filename, '======>', new_name)

# for filename in img_file:
#     if filename == '.DS_Store':
#         continue
#
#     recent_filename = os.path.join(pth,filename)
#     sub_img_filenames = os.listdir(recent_filename)
#     print(recent_filename)


    # if len(sub_img_filenames) == 0:
    #     os.removedirs(recent_filename)
        # continue
    # for num, img_name in enumerate(sub_img_filenames):
    #     if '._' in img_name:
    #         print(img_name)
    #         # os.remove(os.path.join(recent_filename,img_name))
    #         continue
        # old_name = os.path.join(recent_filename,img_name)
        # # print(old_name)
        # new_name = recent_filename+'/'+str(filename)+'_'+str(num)+'.png'
        # # print(new_name)
        # os.rename(old_name, new_name)
        # print(old_name, '======>', new_name)