text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
numbs = text[pos:]
fnumbs = float(numbs)
print (fnumbs)
