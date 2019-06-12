#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 网络获取数据
import requests
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

response = requests.get(url,headers=headers)
html = response.text
# print(html)
# 把响应数据转换成python数据类型
data = json.loads(html)
print(data)
# 使用 jsonpath 提取数据
cities = jsonpath.jsonpath(data,'$..allCitySearchLabels..[?(@.isSelected==False)].name')
print(cities)