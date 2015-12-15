text = "X-DSPAM-Confidence:    0.8475";
spacePos = text.find(" ")
#print spacePos
number = text[spacePos::]
#print number
strippedNumber = number.lstrip();
result = float(strippedNumber)

def reprint(printed):
    print printed  

reprint(result)


