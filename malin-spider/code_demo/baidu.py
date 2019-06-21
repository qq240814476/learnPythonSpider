import requests

url = 'http://www.baidu.com'

response = requests.get(url)

html = response.texta

print('response: %s \nhtml:%s'%(response, html))