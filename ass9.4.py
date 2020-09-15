fname = input("Enter file:")
counts = dict()
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open('mbox-short.txt')
for line in handle :
    if line.startswith('From ') :
        words = line.split()
        name = words[1]
        counts[name] = counts.get(name, 0) + 1

number = None
bigname = None
for name,count in counts.items() :
    if number is None or count > number :
        number = count
        bigname = name
print (bigname, number)
