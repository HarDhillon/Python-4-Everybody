name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
dict = dict()
for line in fhandle :
    if line.startswith('From ') :
        words = line.split()
        #takes the time of the line
        time = words[5]
        #split the time and then take only the hour
        indvtime = time.split(':')
        hour = indvtime[0]
        #create dictionary counting number of time each hour appears
        dict[hour] = dict.get(hour, 0) + 1

list = list()
for k,v in dict.items() :
    #creates a tuple for every key value pair and adds it to a list
    newtup = (k, v)
    list.append(newtup)
#sorts list from biggest to smallest for KEYS
list = sorted(list)
#above is actually accomplished entirely by list = sorted(dict.items())
for k,v in list :
    print (k, v)
