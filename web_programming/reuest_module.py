#!/usr/bin/python3

import requests 

# for practice we use website: https://httpbin.org

response = requests.get('https://httpbin.org/get')

if response.status_code != 200 :
    print("Website not found")
else:
    print("website found: ")
    print(response.status_code)

    # print(response.text)

    # we can convert this response to json
    json_res = response.json()

    del json_res['origin'] # to remove any particular item form json

    print(json_res)

# we can give different parameter(get) or payload(post)

###> params in case of "get"
params = {
    "name":"will",
    "age":"29"
} 
response = requests.get('https://httpbin.org/get', params=params)

print(response.url)

###>  payload in case of "post"
payload = {
    "name":"helloworld",
    "age":"34"
}

response = requests.post('https://httpbin.org/post', data=payload)

print(response.text)

###> changing https headers:

headers = {
    # in here we can specify all the headers we want to change
    'User-Agent':"ghostbrowser/5.0"
}

response = requests.get('https://httpbin.org/get',headers=headers)

print(response.text)

###> download images with request 

headers = {
    "User-Agent":'ghostbrowser/5.0',
    'Accept':'/image/jpeg'
}

response = requests.get("https://httpbin.org/image",headers=headers)

with open("newPic2.jpeg",'wb') as f:
    f.write(response.content)

###> proxy server config:

# proxies = {
#     'http':"173.192.21.89:80",
#     'https': "173.192.21.89:80"
# }

# response = requests.get('http://httpbin.org/get', proxies=proxies)

# print(response.text)