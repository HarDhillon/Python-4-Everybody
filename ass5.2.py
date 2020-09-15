largest = None
smallest = None
sum = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        ival = int(num)
    except :
        print ('Invalid Input')
        continue
    if smallest is None :
        smallest = ival
    elif ival < smallest:
        smallest = ival
    elif largest is None :
        largest = ival
    elif ival > largest :
        largest = ival
    sum = sum + ival


print ("Sum is" , sum)
print("Maximum is", largest)
print ('Minimum is' , smallest)
