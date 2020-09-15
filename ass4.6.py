def computepay(hours , rate) :
    print ('in computepay', hours, rate)
    if hours > 40 :
        normal_pay = hours * rate
        return normal_pay
    else:
        ot = hours - 40
        op = rate * 1.5
        tpay = (40 * rate) + (ot * op)
        return tpay

hrs = input ('Enter Hours: ')
rate = input ('Enter Rate: ')
fh = float(hrs)
fr = float(rate)

p = computepay(fh , fr)

print ("Pay:" , p)
