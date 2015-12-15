files= raw_input("enter file name")
fh=open(files)
for line in fh:
    print line.upper().strip()
    