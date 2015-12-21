
import requests
from bs4 import BeautifulSoup

url = 'http://vnexpress.net'
r = requests.get(url)
r_html = r.text

print (r_html)
#import sys
#print(sys.version_info)



