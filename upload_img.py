import requests
import json
import sys


def upload(token,img_pth):
#    url = 'http://221.8.55.174:8081/prod-api/system/oss/upload'
#     url = 'https://szhmd.mengxist.com:10444/prod-api/system/oss/upload'
    url = 'https://szhmd.mengxist.com:10444/prod-api/file/upload'

    file_name = img_pth.split('/')[-1]
#    print(file_name)
    # payload={}
    files=[
            ('file',(file_name,open(img_pth,'rb'),'application/octet-stream'))
    ]
    headers = {
       'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
       'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, files=files)
    print(response.json())
#    print(response.text)
    #print(response.json()["data"]["url"],type(response.json()["data"]["url"]),len(response.json()["data"]["url"]))
#    print(response.json()["data"]['url'])
#    return(response.json()["data"]['url'])
    return(response.json()['data']["url"])



def key_token():
    url = "https://szhmd.mengxist.com:10444/prod-api/auth/appLogin"

    payload = json.dumps({
        "password": "123456",
        "username": "1049"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['data']["access_token"]
    # print(type(response))
    # print(response.json()["token"])



# ll = key_token()
# print(ll)
#
# ls = upload(ll,'/Users/liufucong/Desktop/WechatIMG23.jpg')
# print(ls)

# def str_to_hex(s):
#     # 文本转16进制
#     return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
# a = "钻石-荷花"
# print(str_to_hex(a))






#方法二

if __name__ == '__main__':
    print(sys.argv[0])