import urllib.request, urllib.parse, urllib.error
import ssl
import json


url = input('Enter location: ')


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data)

info = json.loads(data)
#print(info)

sum = 0


for item in info['comments']:
    num = item['count']
    #num = int(num)
    sum = num + sum

print('Sum: ', sum)
