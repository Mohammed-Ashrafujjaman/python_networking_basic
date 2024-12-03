#!/usr/bin/python3

import urllib.request

url = input("enter an website. example: https://youtube.com :")

http_response = urllib.request.urlopen(url)

if http_response.code == 200 :
	# print(http_response.headers)
	for key, value in http_response.getheaders():
		print(f"{key} ===> {value}")