import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False

if api_key is False:
    api_key = 42
    #this is the first half of the url
    serviceurl = "http://py4e-data.dr-chuck.net/json?"

#will keep prompting for addresses till you hit enter on blank line
while True:
    address = input('*Hit Enter when done* Enter location: ')
    if len(address) < 1: break

#create a dictionary
    parms = dict()
    #first bit of dictionary is {address: address}
    parms['address'] = address
    if api_key is not False:
        #second bit of dictionary {key: (whatever api key we gave, so here, 42)}
        parms['key'] = api_key
    #this will add the address + key to end of our url
    #it will parse and encode it which removes sapces etc making it look like
    #this: address=University+of+Wisconsin&key=42
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    #read and decode all the json we got from the url
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
js = json.loads(data)
#dumps all the json for us to look at if we need
print (json.dumps(js, indent = 4))
#the list only has one thing in it, so we grab the first thing
print (js["results"][0]["place_id"])
