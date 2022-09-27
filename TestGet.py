"""
Author :  FlyTang
File   :  TestGet.py
Date   :  2022/9/27 
Reference  : NONE
Description: In order to complete the daily report, I am going to write a script.
"""
import requests
import time

url = 'https://pingan.ouc.edu.cn/ncov/wap/default/save'

headers = {
    'Host': 'pingan.ouc.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2454',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; V1813A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3209 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/9081 MicroMessenger/8.0.20.2100(0x28001455) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://pingan.ouc.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://pingan.ouc.edu.cn/ncov/wap/default/index',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'eai-sess=30bpcxxxxxxx56l4uga4551; UUkey=921785439xxxxxxxx5331dae756f; Hm_lvt_48b682d4885d22a90111e46b972e3268=1649384695; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1649384695',
}

def getDate():
    time_str = time.strftime('%Y%m%d')
    date = int(time_str) - 1
    print('date:',str(date))
    return str(date);

data = {
    'sfzgsxsx': '0',
    'sfzhbsxsx': '0',
    'ismoved': '0',
    'sfjtfxdq': '0',
    'sfjcfrhxdbr': '0',
    'sfbqzwhz': '0',
    'sfjcqzfyyshz': '0',
    'sfcyglq': '0',
    'sfjchbjwry': '0',
    'szxqsfyqzbl': '0',
    'zrhdgj': '',
    'sfjcfjry': '0',
    'szsqfsyq': '0',
    'oucsfjzym': '1',
    'oucwjzyy': '',
    'oucyzjzpp': '1',
    'oucyzjzwcsj': '',
    'oucezjzpp': '1',
    'oucezjzwcsj': '2021-06-10',
    'oucezjzdd': '1',
    'oucsfyjzjqz': '1',
    'uid': '2xxx5',# 用户标识
    'date': getDate(),#日期：天数减一？？
    'tw': '3',
    'sfcxtz': '0',
    'sfyyjc': '0',
    'jcjgqr': '0',
    'jcjg': '',
    'sfjcbh': '0',
    'sfcxzysx': '0',
    'remark': '',
    'address': '山东省青岛市崂山区沙子口街道敏行西路中国海洋大学崂山校区',
    'area': '山东省 青岛市 崂山区',
    'province': '山东省',
    'city': '青岛市',
    'geo_api_info': '{"status":0,"code":0,"info":"SUCCESS","position":[120.499508,36.165359],"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":48,"isConverted":false,"altitude":null,"altitudeAccuracy":null,"heading":null,"speed":null,"addressComponent":{"citycode":"0532","adcode":"370212","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"松岭路","streetNumber":"290号","province":"山东省","city":"青岛市","district":"崂山区","township":"沙子口街道"},"formattedAddress":"山东省青岛市崂山区沙子口街道敏行西路中国海洋大学崂山校区","roads":[],"crosses":[],"pois":[]}',
    'created': '1649468505',#getCreated(),#提交时间戳#应该是后台自己生成的，这里写死，与后台的数据不一样
    'qksm': '',
    'sfzx': '1',
    'sfjcwhry': '0',
    'gllx': '',
    'glksrq': '',
    'jcbhlx': '',
    'jcbhrq': '',
    'sftjwh': '0',
    'sftjhb': '0',
    'fxyy': '',
    'bztcyy': '',
    'fjsj': '0',
    'sfjchbry': '0',
    'sfjcqz': '',
    'jcqzrq': '',
    'jcwhryfs': '',
    'jchbryfs': '',
    'xjzd': '',
    'szgj': '',
    'sfsfbh': '0',
    'jhfjrq': '',
    'jhfjjtgj': '',
    'jhfjhbcc': '',
    'jhfjsftjwh': '0',
    'jhfjsftjhb': '0',
    'szsqsfybl': '0',
    'sfsqhzjkk': '0',
    'sqhzjkkys': '',
    'sfygtjzzfj': '0',
    'gtjzzfjsj': '',
    'szcs': '',
    'sfqrxxss': '1',
    'id': '11679505',#getId(),#一直在变化，怎么办？#应该是后台自己生成的，这里写死，与后台的数据不一样
    'gwszdd': '',
    'sfyqjzgc': '',
    'jrsfqzys': '',
    'jrsfqzfy': '',
    'szgjcs': ''
}

r = requests.post(url=url, headers=headers, data=data)

print(r.json())#{"e":0,"m":"操作成功","d":{}}
