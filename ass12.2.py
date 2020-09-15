import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen #open urls
from bs4 import BeautifulSoup #import beautifulsoup which parses HTML
import ssl #used for ignoring certification errors


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter Count: ')) #how many repeats
pos = int(input('Enter Position: ')) #position of link

# made a defintion which parses the html
def parsehtml(url, pos) :
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    #finds 'anchor' tags, i.e links
    tags = soup('a')
    i = 0
    #returns tag if tag position matches indicated position
    for tag in tags :
        #following every link it reads it will add 1
        i = i + 1
        if i == pos :
            #returns either the tag, or nothing.
            return tag.get('href', None)

currentnum = 0
#keeps looping until reaches the number of times you asked it to repeat
while currentnum  <= count :
    print ('Retrieving: ', url )
    #runs the function to find the newest url on that page
    url = parsehtml(url, pos)
    currentnum += 1
