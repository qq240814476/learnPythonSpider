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
# print(data)
# 使用 jsonpath 提取数据
# cities = jsonpath.jsonpath(data,'$..allCitySearchLabels..[?(@.isSelected==False)].name')
# print(cities)

smallIdCities = jsonpath.jsonpath(data,'$..allCitySearchLabels..[?(@.id<600)].name')
print(smallIdCities)a

'''
```json
{ 
  "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```
### 语法规则
| 语法         | 描述               | 案例          |
|-------------|-------------------|---------------|
| $           | 根节点             |
| @           | 现行节点           |
| .           | 取子节点           | $.store.book  |
| ..          | 取子孙节点         | $..book        |
| []          | 设置筛选条件        | $..book[0]     |
| [,]         | 支持多选选择内容    | $..book[1,3]     |
| ()          | 支持表达式计算      | $..book[(@.length - 1)]  |
| ?()         | 支持过滤操作        | $..book[?(@.price<10)]    |
'''