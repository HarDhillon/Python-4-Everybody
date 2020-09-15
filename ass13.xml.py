import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen #open urls
from bs4 import BeautifulSoup #import beautifulsoup which parses HTML
import ssl #used for ignoring certification errors
import xml.etree.ElementTree as ET #import XML

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ' )
html = urllib.request.urlopen(url, context=ctx)
data = html.read()

print ('Retrieving ', url)
#returns characters
print ('Retrieved', len(data), 'characters')

#turns the data into readable format to find, e.g removes all the '<>' etc.
tree = ET.fromstring(data)
#creates a list containing all the things in 'comment' which is in 'comments'
list = tree.findall('comments/comment')
#if there was more than one thing under 'comment' the length of list would be wrong
    #you would need to go further and do 'comments/comment/count'
print ('Count:', len(list))
total = 0
for item in list :
    total = total + (int(item.find('count').text))
# note that the above can also be written as:
    #tree = ET.fromstring(data)
    #list = tree.findall('comments/comment/count')
    #print ('Count:', len(list))
    #total = 0
    #for item in list :
    #    total = total + int(item.text)
print (total)
