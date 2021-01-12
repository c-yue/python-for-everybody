# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url1 = input('Enter - ')
count1 = 7
pos1 = 18

#decode text func
def trace(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


#loop name func
def explore(soup, pos):
    tags = soup('a')
    pos_tag = 0
    for tag in tags:
        link = tag.get('href', None)
        pos_tag = pos_tag + 1
        #print(pos_tag)
        if pos_tag == pos:
            break
        else:
            continue
    return link


#main process
count_tag = 0
while count_tag < count1:
    soup1 = trace(url1)
    url1 = explore(soup1, pos1)
    count_tag = count_tag + 1
    #print(count_tag)

print(url1)
