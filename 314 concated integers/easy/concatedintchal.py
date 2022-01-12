#dailyprogrammer 314 easy
#concated integers

from copy import deepcopy
import sys

input = '17 32 91 7 46'
input = input.split(' ')
for i in input:
	i = i.split('')
 
def findmin(x):
	min = 9999
	for i in x:
		j = 0
		while i[j] != min[j]:
			j = j+1
			
		if i[j] < min[j]:
			min = int(i)
			
	return min		
			
	
	
print input
print findmin(input)
