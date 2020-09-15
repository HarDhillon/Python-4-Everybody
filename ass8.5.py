fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
list = []

for line in fh :
    #if line.startswith('From:') :
        #continue
    if line.startswith('From ') :
        adrs = line.split()
        mail = adrs[1]
        print (mail)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
