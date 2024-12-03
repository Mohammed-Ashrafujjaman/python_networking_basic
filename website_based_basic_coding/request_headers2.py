#!/usr/bin/python3

from urllib.request import Request, urlopen

user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20"
url = 'https://youtube.com'

def add_header():
	# creating custom headers for the request in dictionary.
	headers = {'Accept-Language' : 'n1', 'User-agent': user_agent}
	# binding url and headers in a request. more likly custom request.
	request = Request(url, headers=headers)
	# creating actual request to the webstie
	response = urlopen(request)

	for key, value in request.header_items():
		print(f"{key} ===> {value}")
	print(response.status)


if __name__ == "__main__":
	add_header()


# With this we can spof website as we like.
# we can send request from custom headers and get by in many cases.
# we need some more modification to work with the response and show it in browser.
# aside that we need to include session to avoid losing authentication in case of login.
# request library is more advanced than urllib.