times=dict()
time=list()
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname, 'r')
except:
    print "Error opening file", fname
    quit()
count=0    
for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        time=words[5]
        time=time.split(':',0)
        hour=time[0]
        if hour not in times:
            times[hour]=times.get('hour',1)
        else:
            times[hour]=times[hour] + 1    
    else:
        continue
#print times
for key,value in times.items():
    time.append((key,value))   
time.sort()
#print time
for key,value in time[3:]:
  	print key,value