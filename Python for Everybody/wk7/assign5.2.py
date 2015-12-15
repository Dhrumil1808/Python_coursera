largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
       # print "Please enter a number as input or \'done\'"
        print "Invalid input"
        
    if smallest is None:
        smallest = num 
    if largest is None:
        largest = num     
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

print "Maximum is", int(largest)  
print "Minimum is", int(smallest)
