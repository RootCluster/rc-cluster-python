import requests

# url = 'https://httpbin.org/get'
# data = {'key': 'value', 'abc': 'xyz'}
# # .get 是使用get方式请求 url，字典类型的 data 不用进行额外处理
# response = requests.get(url, data)
# print(response.text)

# post 请求
import requests

url = 'https://httpbin.org/post'
data = {'key': 'value', 'abc': "xyz"}
response = requests.post(url, data)
# 返回类型为 json 格式
print(response.json())
