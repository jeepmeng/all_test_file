import glob
import os
import cv2
# import config_101
# import torch
# import numpy as np
# from torch import nn
# from PIL import Image
# from torchvision import models
# import torch.nn.functional as F
# import torchvision.transforms as transforms
import json


# class init_model:
#     def __init__(self, pth='epoch_10145.pth', num_classes=41):
#         self.transform_test = transforms.Compose([
#             transforms.Resize((224, 224)),
#             transforms.RandomHorizontalFlip(),
#             transforms.ToTensor()
#         ])
#
#         self.model = models.resnet101(pretrained=False)
#         self.num_fits = self.model.fc.in_features
#         self.model.fc = nn.Linear(self.num_fits, num_classes)
#         self.model.load_state_dict(torch.load(pth, map_location=torch.device('cpu'))['net'])
#         self.model.to(config_101.device)
#         self.model.eval()
# #         print('kaishile')
#
#     #     self.outputs
#     def predict_images(self, image_file):
# #         image = Image.open(image_file)
# #         image = image.convert("RGB")
# #         img = image.copy()
# #         numpy_array = np.asarray(image.copy())
#         image = self.transform_test(image_file)
#         image = image.unsqueeze_(0).to(config_101.device)
#         with torch.no_grad():
#             outputs = self.model(image)
#             outputs = outputs.to(config_101.device)
#         values_prob,values_index = torch.topk(outputs,config_101.return_num)
#         k_index = values_index.data.cpu().numpy()
#         pro = F.softmax(values_prob[0], dim=0).data.cpu().numpy()
#
#         return k_index,pro
#
#
#     def test_predict_images(self, image_file):
#         image = Image.open(image_file)
#         image = image.convert("RGB")
#         img = image.copy()
# #         numpy_array = np.asarray(image.copy())
#         image = self.transform_test(img)
#         image = image.unsqueeze_(0).to(config_101.device)
#         with torch.no_grad():
#             outputs = self.model(image)
#             outputs = outputs.to(config_101.device)
#         values_prob,values_index = torch.topk(outputs,10)
#         k_index = values_index.data.cpu().numpy()
#         pro = F.softmax(values_prob[0], dim=0).data.cpu().numpy()
#
#         return k_index,pro




if __name__ == '__main__':
#     pth = 'data2/epoch_10145.pth'
    img_pth = '/Users/liufucong/Downloads/jlyc/image/中华(双中支)-整条.jpg'
#     img_pth2 = '/Users/liufucong/Downloads/jlyc/image/长白山(蓝尚)-整条.jpg'
#     img_pth3 = '/home/xht/danhe_zq/changbaishan_777/jiaodu/angle_move_IMG_5824.jpg'
#     #     get_image_label_to_predict(img_pth3)
#
#     aa = init_model()
#     k_index,pro = aa.predict_images(img_pth3)
#     print('k_index------------',k_index)
# #     print('duo-------------',duo)
#     print('pro------------',pro)







    ll = cv2.imread(img_pth)
    print(ll[50,150:200,1])
    # print(ll)
