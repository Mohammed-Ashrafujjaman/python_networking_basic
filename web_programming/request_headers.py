#!/usr/bin/python3

### to understand request better see "request_module.py"  
### Request headers :
#   Accept
#   Accept-Encoding
#   Accept-Language
#   Connection
#   Host
#   Upgrade-Insecure-Request
#   User-Agent
#   << there are a few more >>

import urllib.request as urlreq
from urllib.request import Request

url = "https://www.youtube.com"
# !* urlopen can get some info but incase of https headers we need "request"  *!

req = Request(url) # in here after url we can provide: headers(dict), data, timeout
http_response = urlreq.urlopen(req)

print(req.get_header('User-agent'))
# to see all the header item
print(req.header_items())
# to add new header item
req.add_header('Accept-Language','en')

print(req.header_items())


# print(http_response)

if http_response.code == 200:
    print(http_response)