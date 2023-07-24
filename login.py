# import requests
# import json
#
#
#
# def upload(token,img_pth):
#     url = 'http://221.8.55.174:8081/prod-api/system/oss/upload'
#
#
#     # payload={}
#     files=[
#        ('file',('<file>',open(img_pth,'rb'),'application/octet-stream'))
#     ]
#     headers = {
#        'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
#        'Authorization': token
#     }
#
#     response = requests.request("POST", url, headers=headers, files=files)
#
#     print(response.text)
#     return(response.json()["data"])
#
#
#
# def key_token():
#     url = "http://221.8.55.174:8081/prod-api/business/appLogin/login"
#
#     payload = json.dumps({
#         "password": "123456",
#         "username": "1049"
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     print('token-------------',response.json()["token"])
#     return response.json()["token"]
#
# img_pth = '/Users/liufucong/Desktop/截屏2023-04-12 14.28.34.png'
# ll = key_token()
# print(ll)
# #
# ls = upload(ll,img_pth)
# print(ls)




import requests
import json



def upload(token,img_pth):
    url = 'http://221.8.55.174:8081/prod-api/system/oss/upload'


    # payload={}
    files=[
       ('file',('<file>',open(img_pth,'rb'),'application/octet-stream'))
    ]
    headers = {
       'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
       'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, files=files)

    #print(response.text)
    #print(response.json()["data"]["url"],type(response.json()["data"]["url"]),len(response.json()["data"]["url"]))
    return(response.json()["data"]["url"])



def key_token():
    #url = "http://192.168.100.104:8080/prod-api/business/appLogin/login"
    url = "http://221.8.55.174:8081/prod-api/business/appLogin/login"

    payload = json.dumps({
        "password": "123456",
        "username": "1049"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("aaa")
    print('token-------------',response.json()["token"])
    return response.json()["token"]
    # print(type(response))
    # print(response.json()["token"])



ll = key_token()
#print(ll)
#
ls = upload(ll,'/Users/liufucong/Desktop/截屏2023-04-12 14.28.34.png')
#print(ls)























