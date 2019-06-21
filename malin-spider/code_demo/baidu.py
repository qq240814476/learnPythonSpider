import requests

url = 'http://www.baidu.com'

response = requests.get(url)

html = response.text

print('response: %s \nhtml:%s'%(response, html))