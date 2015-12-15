fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    if line.startswith('From:'):
       count=count+1
       split=line.split();
       print split[1]
    if not line.startswith('From:'):
        continue
    
       
print "There were", count, "lines in the file with From as the first word"
