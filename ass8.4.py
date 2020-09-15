fname = input("Enter file name: ")
list = list()
fh = open(fname)
for line in fh :
    words = line.split()
    for word in words :
        if word not in list :
            list.append(word)
list.sort()
print (list)
