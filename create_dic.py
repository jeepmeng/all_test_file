import os
import json
pth_1 = '/Volumes/T7/烟草抠图/dict_2.txt'


# f = open(pth_1)
# for line2 in pth_1:
#     print(line2)

# dic = {}
#
# with open(pth_1) as f:
# # f = open("c:\\1.txt","r")
#     lines = f.readlines()      #读取全部内容 ，并以列表方式返回
#     for line in lines:
#         # print(line)
#         line = line.strip('\n')
#         img_name,index = line.split(',')
#         print(img_name)
#         # index = line.split(',')[0]
#         dic[img_name] = index
# b = json.dumps(dic, ensure_ascii=False)
# with open('/Volumes/T7/烟草抠图/dic_json_2.json', 'w', encoding='utf-8') as f:
#     f.write(b)


dict = dict()
# print(dict)

# pth_json_1 = '/Volumes/T7/烟草抠图/dic_json_1.json'
pth_json_1 = '/Users/liufucong/Downloads/dic_json_train_val.json'
pth_json_2 = '/Users/liufucong/Downloads/dic_json_1.json'
with open(pth_json_1) as f1, open (pth_json_2) as f2:
# file_1 =
    content_1 = f1.read()
    file_1 = json.loads(content_1)
    ori_dict = file_1.keys()

    content_2 = f2.read()
    file_2 = json.loads(content_2)
    delete_dict = file_2.keys()
    # print(file_2.keys())
    for i in ori_dict:
        for k in delete_dict:

            if file_1[i] == file_2[k]:
                print('{}========{}'.format(i,k))
                dict[i]=[k,110106,6901028071475]
                continue
print(dict)

b = json.dumps(dict, ensure_ascii=False)
with open('/Users/liufucong/Downloads/dic_json_xiugaihou.json', 'w') as f:
    f.write(b)
