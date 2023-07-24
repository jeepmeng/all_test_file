from flask import Flask, request
import requests

import itertools

# 16项因素权重比
shop_mark_pro_weight = {
    "focus_on_monitoring_customers": 0.1,
    "standardized_business_records": 0.1,
    "digital_intelligence_signing_data": 0.1,
    "four_member_coordination": 0.1,
    "integrity_rating": 0.1,
    "terminal_data": 0.1,
    "excellent_team_leader": 0.1,
    "leader": 0.1,
    "competency_label": 0.1,
    "order_volume": 0.1,
    "customer_format": 0.1,
    "customer_gear": 0.1,
    "new_onboarders": 0.1,
    "sudden_factors": 0.1,
    "customer_proactive_demand": 0.1,
    "customer_complaint_consultation": 0.1,
}


# 速度优先下通过起止点和终止点，途经点给出多种最佳路线
def best_map_speed(start, end, *args, strategy=0):
    """
    :param start:起始点
    :param end: 目的点
    :param tujingdian:途经点
    :param strategy: 速度优先计算导航距离
    :return: 最佳速度优先导航路线
    """
    parameters = {'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                  'origin': start,
                  'destination': end,
                  'waypoints': args,
                  'strategy': strategy,
                  }  # 地址参数
    url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
    # print(result)
    # print(lon_lat)
    return lon_lat


class Place:

    def __init__(self, emgerncy):
        self.emgerncy_1 = emgerncy[0]
        self.emgerncy_2 = emgerncy[1]
        self.emgerncy_3 = emgerncy[2]


# 返回地点经纬度，两点间距离
class lxgh:
    def __init__(self):
        pass

    def place_distance(addr1, addr2):
        """
        :param addr1:起始点
        :param addr2: 终止点
        :return: 两点距离
        """
        parameters = {'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                      'origin': addr1,
                      'destination': addr2,
                      }  # 地址参数
        url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
        # print("walking规划",result)
        # print(lon_lat)
        return lon_lat

    # 最终计算按顺序给出所有路线
    def mix_all_place(self, jinji_list, huanman_list):
        shunxu_list = []
        if len(jinji_list) == 1 and len(huanman_list) > 1:
            shunxu_list.append(jinji_list[0])

        if len(huanman_list) < 1 and len(jinji_list) > 1:
            return jinji_list[:-1], jinji_list[-1]
        if len(jinji_list) < 1 and len(huanman_list) > 1:
            return huanman_list[:-1], huanman_list[-1]
        else:
            for i in jinji_list:
                shunxu_list.append(self.place_zuobiao(i))
            for j in huanman_list:
                shunxu_list.append(self.place_zuobiao(j))
        # print("all_place",shunxu_list)
        return shunxu_list[:-1], shunxu_list[-1]

    # 分配紧急和不紧急地点
    def jisuan_line(self, all_place):
        jinji_list = []
        huanman_list = []
        for i in all_place:
            # print(i)
            if Place(i[1], i[2]).emgerncy == "紧急" or Place(i[1], i[2]).deadline == "2day":
                jinji_list.append(i[0])
            else:
                huanman_list.append(i[0])
        return jinji_list, huanman_list

    # 距离优先下通过起止点和终止点，途经点给出多种最佳路线
    def best_map_less_distance(self, start, end, *args):
        """
        :param start: 起始点
        :param end: 目的点
        :param tujingdian:途经点
        :param strategy: 距离优先
        :return: 返回距离最短计算导航
        """
        #         a2 = 1
        #         print('start----------------',start)
        #         print('end ----------------',end)
        #         print('args----------------',args)
        # print("xx")
        parameters = {'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                      'origin': start,
                      'destination': end,
                      'waypoints': args,
                      'strategy': 2,
                      }  # 地址参数
        #         a1 = 1
        url = 'https://restapi.amap.com/v3/direction/driving?'  # 高德地图地理编码API服务地址

        result = requests.get(url, parameters)  # GET方式请求
        # print("cccc")
        result = result.json()
        #         print('result key---------------',result.keys())
        # return result
        try:
            lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
        except Exception as e:
            print("error")
        # 获取返回参数geocodes中的location，即经纬度
        # print("路径规划", result)
        return lon_lat

    def place_zuobiao(self, addr):
        """
        :param addr: 导航地点
        :return: 地点经纬度坐标
        """

        para = {'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                'address': addr}  # 地址参数
        url = 'https://restapi.amap.com/v3/geocode/geo?'  # 高德地图地理编码API服务地址
        result = requests.get(url, para)  # GET方式请求
        result = result.json()
        # print("result",result)
        try:
            lon_lat = result['geocodes'][0]['location']  # 获取返回参数geocodes中的location，即经纬度
        except Exception as e:
            print("error", addr)
        # print("地点经纬度",lon_lat,type(lon_lat))
        return lon_lat

    def base_time(self, start, place_list):
        jj_list, hm_list = self.jisuan_line(place_list)
        middle, end = self.mix_all_place(jj_list, hm_list)

        return self.best_map_less_distance(self.place_zuobiao(start), end, middle)

    def all_path(self, data_json):
        start = data_json['start'][0] + ',' + data_json['start'][1]

        data_middle = []
        #         name_middle = []
        for i in data_json['middle']:
            kk = i['lng'] + ',' + i['lat']
            route_name = i['name']
            addr_name = i['addr']
            #             name_middle.append(route_name)
            data_middle.append([addr_name, route_name, kk])

        new_list = []
        for data in itertools.permutations(data_middle, len(data_middle)):
            new_list.append(list(data))

        distance_all = []
        for i in new_list:
            distance = self.best_map_less_distance(start, i[1][-1], i[1][:-1])
            distance_all.append(int(distance))

        data_zip = list(zip(new_list, distance_all))
        data_zip.sort(key=lambda x: x[1])
        #         print(data_zip)
        #         print('data_zip[0]=--------------',data_zip[0][0])
        for i, k in enumerate(data_zip[0][0]):
            #             print('k---------------------',k)
            data_json['middle'][i]['order'] = i + 1
            data_json['middle'][i]['lng'] = k[2].split(',')[0]
            data_json['middle'][i]['lat'] = k[2].split(',')[1]
            data_json['middle'][i]['name'] = k[1]
            data_json['middle'][i]['addr'] = k[0]
        return data_json

    def pri_path(self, data_json):

        #         start = data_json['start']

        data_middle_addr = []
        data_middle_urgent = []
        data_middle_name = []
        addr_middle_name = []
        for i in data_json['middle']:
            kk = i['lng'] + ',' + i['lat']
            data_name = i['name']
            data_middle_name.append(data_name)
            data_middle_addr.append(kk)
            data_middle_urgent.append(i['urgent'])

        data_zip = list(zip(addr_middle_name, data_middle_name, data_middle_addr, data_middle_urgent))
        data_zip.sort(key=lambda x: (-x[3][0], -x[3][1], -x[3][2]))

        for j, i in enumerate(data_zip):
            #             print(i)
            data_json['middle'][j]['lng'] = i[2].split(',')[0]
            data_json['middle'][j]['lat'] = i[2].split(',')[1]
            data_json['middle'][j]['order'] = j + 1
            data_json['middle'][j]['name'] = i[1]
            data_json['middle'][j]['addr'] = i[0]

        return data_json


if __name__ == '__main__':
    yancao = lxgh()

    ccc = {
    'mark': "distance",
    'start': [
        "125.260648",
        "43.881469"
    ],
    'middle': [
        {
            "order": '',
            "name": "南关区源通新天地超市",
            "addr": "吉林省长春市南关区南环城路以南、亚泰大街以东省女子劳教所地块棚户区改造项目（新星宇·之洲上邻）A-3地块第2【幢】【座】0【单元】【层】116、117号房（9815）",
            "id": 133,
            "lat": "43.816121",
            "lng": "125.340347",
            "urgent": ''
        },
        {
            "order": '',
            "name": "南关区霞姐超市",
            "addr": "吉林省长春市南关区东岭北街煤气宿舍10栋2门104室",
            "id": 233,
            "lat": "43.870519",
            "lng": "125.352382",
            "urgent": [
                5,
                3,
                1
            ]
        },
        {
            "order": '',
            "name": "南关区聚家福超市",
            "addr": "吉林省长春市南关区平康小区8栋106号房",
            "id": 333,
            "lat": "43.886142",
            "lng": "125.330573",
            "urgent": [
                5,
                3,
                1
            ]
        }
    ]
}

    #     for i in cccc['middle']:
    #         print(i)
    #         kk = i['lng']+','+i['lat']
    # #     print(cccc['middle'][0]['lng']+','+cccc['middle'][0]['lat'])
    #         print(kk)

    #     kk =  yancao.all_path(ccc)
    #     print(kk)
    # ll = yancao.pri_path(ccc)
    # print(ll)

    ll = yancao.place_distance("125.330573，43.886142","125.352382，43.870519")
    print(ll)
