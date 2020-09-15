count = 0
sum = 0
print ('before:' , count, sum)
for values in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] :
    count = count + 1
    sum = sum + values
    print (count, sum, values)
print (count, sum, sum / count)
