import re

file = open('ass11.txt')
fileread = file.read()
numbs = re.findall('[0-9]+', fileread)
x = 0
for sum in numbs :
    #convert each number from string into integer
    inumbs = int(sum)
    #adds each integer together for the sum which is x
    x = x + inumbs
print (x)
