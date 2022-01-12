#dailyprogrammer 374
#additive

import sys

def persistance(n, i):
	if n<10:
		return(i)
	a = 0
	while n > 0:
		a += n%10
		n = int(n//10)
	return(persistance(a,i+1))

x = int(sys.argv[1])	
print('The persistance of', x, 'is', (persistance(x,0)))