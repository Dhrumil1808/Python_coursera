def computepay(h,r):
    if(h>40):
        r= r * 1.5 
    else:
        r = r;
    return r        
        

hrs = raw_input("Enter Hours:")
h=float(hrs)
rate=raw_input("Enter rate per hour")
r=float(rate)

if(h<=40):
    pay=h* computepay(h,r)
else:
    pay=40 * r + (h-40) * computepay(h,r)
    
    
print pay