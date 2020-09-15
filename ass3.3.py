score = input('Enter Score: ')
try:
    fs = float(score)
except:
    print ('Please enter a numerical value between 0.0 and 1.0')
    continue
if fs > 1 :
    print ('Please enter a value between 0.0 and 1.0')
    continue

elif fs < 0 :
    print ('please enter a value between 0.0 and 1.0')
    quit()

elif fs >= 0.9 :
    print ('A')
elif fs >= 0.8 :
    print ('B')
elif fs >= 0.7 :
    print ('C')
elif fs >= 0.6 :
    print ('D')
elif fs < 0.6 :
    print ('F')
