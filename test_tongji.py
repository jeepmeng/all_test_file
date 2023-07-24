import json
import run_detect_api
import yanhe_predict
import cv2
from PIL import Image
import detect_with_API
import numpy as np


# def str_to_hex(s):
#     # 文本转16进制
#     return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
# # a = "钻石-荷花"

class img_pred():
    def __init__(self, pre_model):
        #         self.glass_yanhe = [i for i in pre_model.predict_images(glass_yanhe)]
        #         self.huojia_yanhe = [i for i in pre_model.predict_images(huojia_yanhe)]

        self.model = pre_model

    def yanhetj(self, img, glass_yanhe, huojia_yanhe):
        #         print('len(glass_yanhe)--------------',len(glass_yanhe))
        #         print('len(huojia_yanhe)--------------',len(huojia_yanhe))

        img_new = img

        dict_list = list()
        all_label_huojia = {}
        all_label_glass = {}
        probb_count = {}
        dict_empty = dict(status=True, name='unrec', count=0)
        with open('dic_json.json', 'r') as f:
            content = f.read()
            dic_json = json.loads(content)

        if len(huojia_yanhe) >= 1:

            huojia_label_count = []

            for i in huojia_yanhe:
                img_pil = Image.fromarray(cv2.cvtColor(img_new, cv2.COLOR_BGR2RGB))
                huojia_label, huojia_probb = self.model.predict_images(img_pil.crop(i))

                huojia_label_count.append(huojia_label)
                if huojia_probb <= 0.6:
                    #                     huojia_label_count.append(huojia_label)
                    probb_count[huojia_label] = False
            #                 else:
            # #                     huojia_label_count.append(huojia_label)
            #                     huojia_probb_count.append(True)

            for i in huojia_label_count:
                all_label_huojia[i] = huojia_label_count.count(i) * 5

        if len(glass_yanhe) >= 1:

            glass_label_count = []

            for i in glass_yanhe:

                img_pil = Image.fromarray(cv2.cvtColor(img_new, cv2.COLOR_BGR2RGB))
                gls_label, gls_probb = self.model.predict_images(img_pil.crop(i))

                glass_label_count.append(gls_label)
                if gls_probb <= 0.6:
                    probb_count[gls_label] = False

            for i in glass_label_count:
                all_label_glass[i] = glass_label_count.count(i)

        for k, v in all_label_glass.items():
            if k in all_label_huojia.keys():
                all_label_huojia[k] = all_label_huojia[k] + v
            #                     all_label_huojia[k] = all_label_huojia[k][1] & v[1]
            else:
                all_label_huojia[k] = v

        #             print('dict_list-----------',dict_list)

        print(all_label_huojia)
        for i, j in all_label_huojia.items():
            if i in all_label_huojia.keys():
                dict_empty['status'] = False
            else:
                dict_empty['status'] = True

            dict_empty['name'] = dic_json[i]
            dict_empty['count'] = j

        return [dict_empty]


class to_bytes:
    def __init__(self, img):
        self.img = img

    #         self.pil_data = ''
    #         self.npy_data = ''
    def pil_image_to_binary(self):
        """
        将PIL图片转换为二进制数据
        """
        with io.BytesIO() as output:
            self.img.save(output, format='PNG')
            binary_data = output.getvalue()
        return binary_data

    def numpy_array_to_binary(self):
        """
        将numpy数组转换为二进制数据
        """
        binary_data = self.img.tobytes()
        return binary_data

    def return_data(self):
        if isinstance(self.img, np.ndarray):
            final_data = self.numpy_array_to_binary()
            return json.dumps(final_data.decode('ISO-8859-1'))
        elif isinstance(self.img, Image.Image):
            final_data = self.pil_image_to_binary()
            return json.dumps(final_data.decode('ISO-8859-1'))
        else:
            return 'error'


#     print("hello")

if __name__ == "__main__":

    hh = yanhe_predict.init_model()
    aa = detect_with_API.detectapi(weights='/home/xht/yolov7/runs/train/exp14/weights/yancao_0415_02.pt')
    img_cv = cv2.imread("./IMG_4387.jpg")

    result, names = aa.detect([img_cv])
    #     img = result[0][0]
    huojia_yanhe, _ = run_detect_api.ImageLabelList(result[0][1]).huojia_yanhe_tiao()
    #     print(huojia_yanhe)
    glass_yanhe = run_detect_api.ImageLabelList(result[0][1]).glass_yanhe()
    print(glass_yanhe)
    #      = ImageLabelList(result[0][1])

    jieguo = img_pred(hh)
    aa = jieguo.img_pred_bendi(img_cv, glass_yanhe, huojia_yanhe)
    for i in aa.items():
        print(i)
#     print(aa)


#     with torch.no_grad():

#         print("eeee", e.all_result)
#         c = ImageLabelList(result[0][1]).glass_yanhe(result[0][1])
#         print("a", a)
#         print("b", b)
#         print("c", c)
#         for cls, (x1, y1, x2, y2), conf in result[0][1]:
#             print(names[cls], x1, y1, x2, y2, conf)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0))
#             cv2.putText(img, names[cls], (x1, y1 - 20), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0))
#             cv2.imwrite("./run_api/test_1.jpg", img)


#     img_pth3 = '/home/xht/danhe_zq/changbaishan_777/jiaodu/angle_move_IMG_5824.jpg'
#     image = Image.open(img_pth3)
# #     image = image.convert("RGB")


#     img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)


#     cv2.imshow('hh',img)
#     cv2.waitKey(0)


