import ffmpeg
import cv2
import os
import ffmpy



# # 需要转换格式的视频文件，文件真实存在
# source_file = r"/Volumes/T7/IMG_9985.MOV"
# # 转换成功后的视频文件，文件夹真实存在，不会自动创建
# sink_file = r"/Volumes/T7/IMG_9985.mp4"
#
# ff = ffmpy.FFmpeg(
#      inputs = {source_file: None},
#      outputs = {sink_file: None})
# ff.run()


#
# cameraCapture = cv2.VideoCapture('/Users/liufucong/Downloads/97a9d0beeab55b14047c4ddfd02bda35_0_1683612198.mp4')
#
#
# print(cameraCapture.get(cv2.CAP_PROP_FPS))
# print(cameraCapture.get(cv2.CAP_PROP_FRAME_COUNT))
# print(cameraCapture.get(cv2.CAP_PROP_POS_AVI_RATIO))
# print(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap = cv2.VideoCapture('/Users/liufucong/Downloads/97a9d0beeab55b14047c4ddfd02bda35_0_1683612198.mp4')
# 用于保存视频的VideoWriter
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
# fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out = cv2.VideoWriter('/Users/liufucong/Downloads/test_cv2_zhenlv30.mp4', 0x31637661, 30, (int(cap.get(3)), int(cap.get(4))))
while cap.isOpened():
     (ret, frame) = cap.read()
     if ret == True:
          # with torch.no_grad():
          # frame = cv2.cvtColor(frame)
          # result, names = aa.detect([frame])
          # new_img = result[0][0]

          frame = cv2.resize(frame, (int(cap.get(3)), int(cap.get(4))))
          out.write(frame)
     else:
          break
cap.release()
out.release()
cv2.destroyAllWindows()