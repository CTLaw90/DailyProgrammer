#dailyprogrammer 314 easy
#concated integers

from copy import deepcopy
import sys

input = '17 32 91 7 46'
input = input.split(' ')
for i in input:
	i = int(i)
 
min = 99999999999999999
max = -1

def concate(x, rem):
	global min, max
	print x, rem
	
	if len(rem) == 1:
		c = int(str(x)+str(rem[0]))
		print c
		if c < min:
			min = c
		elif c > max:
			max = c
		
	for i in xrange(len(rem)):
		y = deepcopy(rem)
		y.pop(i)
		concate(x+str(rem[i]), y)
	
	
print input
concate('', input)
print 'min', min, 'max', max