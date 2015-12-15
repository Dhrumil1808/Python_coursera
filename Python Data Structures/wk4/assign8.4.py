fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    line_split=line.split()
    for split in line_split:
        if(split in lst):
            continue
        lst.append(split)
        #print lst
lst.sort()       
print lst