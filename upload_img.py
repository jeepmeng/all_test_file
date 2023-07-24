import requests
import json



def upload(token):
    url = 'http://221.8.55.174:8081/prod-api/system/oss/upload'


    # payload={}
    files=[
       ('file',('<file>',open('/Users/liufucong/Desktop/2023-04-25_14_20_24.jpg','rb'),'application/octet-stream'))
    ]
    headers = {
       'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
       'Authorization': token
    }

    response = requests.request("POST", url, headers=headers, files=files)

    print(response.text)
    return(response.json()["data"])
    # print(response.json)


def key_token():
    url = "http://221.8.55.174:8081/prod-api/business/appLogin/login"

    payload = json.dumps({
        "password": "123456",
        "username": "1049"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["token"]
    # print(type(response))
    # print(response.json()["token"])



# ll = key_token()
# print(ll)
#
# ls = upload(ll)
# print(ls)

# def str_to_hex(s):
#     # 文本转16进制
#     return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
# a = "钻石-荷花"
# print(str_to_hex(a))






#方法二
List_1 =[1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5]




List_2 = [1,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,6]

d1 = {}
d2 = {}
for i in List_1:
    d1[i] = [List_1.count(i),False]


for i in List_2:
    d2[i] = [List_2.count(i),True]


print(d1)

print(d2)

# ll= dict(d1, **d2)
#
# print(ll)
for k, v in d2.items():
    if k in d1.keys():
        d1[k][0] = d1[k][0]+v[0]
        d1[k][1] = d1[k][1] & v[1]
    else:
        d1[k]=v


# d1.update(d2)
# dict(d1.items() + d2.items())
print(d1)


# print('d1-----------------',d1)
# for i in d1.items():
#     print(type(i[0]))
# print(d1.items())

# huojia_label = [1,2,3,4,5]
#
# a = dict(cls=str(2),whole_label=huojia_label)
# print(a)
import matplotlib.pyplot as plt
tt = []
with open('/Users/liufucong/Desktop/epoch_acc.txt','r') as f:
    data = f.read().splitlines()
    # print(data)
for i in data:
    tt.append(int(i*10))

iters = range(100)

plt.figure()
plt.plot(iters,tt, 'red', linewidth = 2, label='train loss')
plt.show()