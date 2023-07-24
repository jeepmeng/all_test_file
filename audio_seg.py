from pydub import AudioSegment
#音频的原始文件record.wav
filename='record'
#读取音频文件
pth = '/Users/liufucong/Downloads/audio_seg/20230627102918400/'
# wav = AudioSegment.from_wav('/Users/liufucong/Downloads/audio_seg/OFIDUD6RBJ_20230627104904400.wav')
# wav = AudioSegment.from_wav('/Users/liufucong/Downloads/audio_seg/OFIDUDN7GI_20230627111400134.wav')
wav = AudioSegment.from_wav('/Users/liufucong/Downloads/audio_seg/OFIDUBI3RE_20230627102918400.wav')



print(len(wav))
#读取前45分钟的音频并保存在record_cut1.wav中
# wav[:45*60*1000].export(filename+'_cut1.wav', format="wav") ​
# #读取45分钟以后的音频并保存在record_cut2.wav中
for i in range(0,333440,100000):
    print(i)
    if i==300000:
        wav[i:].export(pth + '20230627102918400--------' + 'end' + '_cut.wav', format="wav")
    else:
        wav[i:(i+100000)].export(pth+'20230627102918400--------'+str(i+1)+'_cut.wav', format="wav")