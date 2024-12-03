#!/usr/bin/pyhton3

# This code will extract all the links from any given website
#  *! could be used as crawler if rewrite for making a crawler !* 

from html.parser import HTMLParser
import urllib.request as urlreq

class pyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for a in attrs:
                # print(a)
                if a[0] == 'href':
                    link = a[1]
                    if link.find('http') >= 0:
                        print(link)
                        newParser = pyParser()
                        newParser.feed(link)


# url = input("url (include https://): ")
url = "https://www.facebook.com"
request = urlreq.urlopen(url)
parser = pyParser()
parser.feed(request.read().decode('utf-8'))