#n this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL,
#read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#没用的API，有用的URL
api_key = 42
url = 'http://py4e-data.dr-chuck.net/comments_286454.xml?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#读URL
uh = urllib.request.urlopen(url, context=ctx)


#ET解译XML，读树节点，文字化并求和

data = uh.read()
#print(data.decode())
tree = ET.fromstring(data)

sum = 0

lst = tree.findall('comments/comment')
for item in lst:
    num = item.find('count').text
    num = int(num)
    sum = sum + num

print(sum)
