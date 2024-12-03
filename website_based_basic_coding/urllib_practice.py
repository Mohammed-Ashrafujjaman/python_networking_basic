#!/usr/bin/python3
 
# request
#   request code 100: informational, 200: success 
#                300: redirection, 400: client error 
#                500: server error
# Error handling
 


from urllib.request import urlopen
import urllib.error as urlerr

def main():
    try: 
        response = urlopen('http://www.ietf.org/rfc/rfc0.txt',timeout=5)
        print(response.status)
    except urlerr.HTTPError as e:
        print(f"Exception: {e}")
        print(f"reason: {e.reason}")
        print(f"url :{e.url}")
    except urlerr.URLError as e:
        print(f"Exception: {e}")
        print(f"reason: {e.reason}")
        print(f"url :{e.url}")

if __name__ == '__main__':
    main()
