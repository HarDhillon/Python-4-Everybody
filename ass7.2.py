# Use the file name mbox-short.txt as the file name
ival = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    pos = line.find(':')
    numbs = line[pos+1:]
    ival = ival + float(numbs)
avg = ival / count
print ("Average spam confidence:" ,avg)
