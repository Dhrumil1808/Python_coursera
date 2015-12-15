# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count=raw_input('Enter count')
count_int=int(count)
position=raw_input('Enter position')
position_int=int(position)
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
j=0;
# Retrieve all of the anchor tags

while j!=count_int:
	tags = soup('a')
	j=j+1
	i=0;
	for tag in tags:
	    i=i+1
	    #print i
	    tag.contents[0]
	    tag.get('href',None)
	    if i==position_int:
		    name=tag.contents[0]
		    link=tag.get('href',None)
		    print link
		    html=urllib.urlopen(link).read()
		    soup= BeautifulSoup(html)

print name
		

		