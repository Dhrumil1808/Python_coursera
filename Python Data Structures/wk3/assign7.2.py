# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
sum=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count=count+1    
    find=line.find(' ')
    str=line[find::]
    num=str.strip()
    float_num=float(num)
    sum= sum + float_num
    
print "Average spam confidence:",float(sum)/count