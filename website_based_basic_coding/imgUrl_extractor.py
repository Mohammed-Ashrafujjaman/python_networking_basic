#!/usr/bin/python3

from urllib.request import urlopen, urljoin
import re

def extract_img_url(site_res):
    img_regex = re.compile('<img [^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    return img_regex.findall(site_res)

def main():
    url = "https://unsplash.com"
    response = urlopen(url).read().decode('utf-8')
 
    img_list = extract_img_url(response)
    for src in img_list:
        print(urljoin(url,src))


if __name__=='__main__':
    main()