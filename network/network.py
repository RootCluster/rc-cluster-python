from urllib import request
from urllib import parse
import socket
import urllib

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')

response_post = request.urlopen('https://httpbin.org/post', data=data)
print(response_post.read().decode('utf-8'))

try:
    response_get = request.urlopen('https://httpbin.org/get', timeout=1)
    print(response_get.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')
