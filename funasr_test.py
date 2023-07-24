from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import os


inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model='damo/speech_UniASR_asr_2pass-cn-dialect-16k-vocab8358-tensorflow1-online')


ori_pth = '/Users/liufucong/Downloads/测试语音_2023_06_26'

# files = os.listdir(ori_pth)
#
with open('/Users/liufucong/Downloads/data.txt','a+') as f:




with open('./data.txt','a+') as f:

#     for i in files:
#         file_pth = os.path.join(ori_pth,i)
#         wav = os.listdir(file_pth)
#         for j in wav:
#             wav_pth = os.path.join(file_pth,j)
#
#             rec_result = inference_pipeline(
#                 audio_in=wav_pth)
#             try:
#                 f.write(rec_result['text'])
#                 f.write('\n')
#             except Exception:
#                 f.write('UNOCR')
#                 f.write('\n')


    rec_result = inference_pipeline(audio_in='/Users/liufucong/Downloads/asr_test/2023062600000658/2023062600000658.wav')
    f.write('2023062600000658.wav:--------'+'\n')
    f.write(rec_result['text'])
    f.write('\n')
    # print(type(rec_result))
    # print(rec_result)