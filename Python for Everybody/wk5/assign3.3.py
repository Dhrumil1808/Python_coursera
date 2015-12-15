score=raw_input("Enter a number between 0 and 1");
s=float(score);

if(s>=0.9 and s<=1):
    print "A"
elif(s>=0.8):
    print "B"
elif(s>=0.7):
    print "C"
elif(s>=0.6):
    print "D"
elif(s<0.6):
    print "F"
else:
    print "Number is not between 0 and 1"
