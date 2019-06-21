import requests

url = 'http://www.baidu.com'

response = requests.get(url)

html = response.text
content = response.content
staus = response.status_code
requestHead = response.request.headers
request = response.request
headers = response.headers
cookie = response.cookies

# print('response: %s \nhtml:%s'%(response, html))

print('content: %s'%(content))

# print('response: %s \nhtml:%s'%(response, staus))

# print('response: %s \nhtml:%s'%(response, requestHead))

# print('response: %s \nhtml:%s'%(response, request))

# print('response: %s \nhtml:%s'%(response, headers))

# print('response: %s \nhtml:%s'%(response, cookie))
