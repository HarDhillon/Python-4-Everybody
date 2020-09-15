import urllib.request, urllib.parse, urllib.error
import ssl #used for ignoring certification errors
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location:', )
print ("Retrieving", url)

html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()
print ("Retrieved", len(data), "characters")
info = json.loads(data)
#below will print out json so you can see it, if needed
#print (json.dumps(info, indent=2))

sum = 0
list = info["comments"]
print ("Count:", len(list))

for item in list :
    num = int(item["count"])
    sum += num
print ("Sum:", sum)
