import re
fh=open("regex_sum_189303.txt");
s=0;
for line in fh:
	y=re.findall('([0-9]+)',line)
	y=map(int,y)
	#print sum(y)
	s=s +sum(y)

print s
