#magic squares
from math import sqrt

input = [8,11,14,1,13,2,7,12,3,16,9,6,10,5,4,15]

#grid length
n = int(sqrt(len(input)))
magic = True

goal = ((1 + n**2) * n) / 2



#col
for row in xrange(n):
	sum = 0
	for col in xrange(n):
		sum += input[row + (n*col)]
		
	if sum != goal:
		magic = False
		break
		
#row
if magic == True:
	for row in xrange(n):
		sum = 0
		for col in xrange(n):
			sum += input[(n*row) + col]
			
		if sum != goal:
			magic = False
			break
			
#diag1
if magic == True:
	sum = 0
	for col in xrange(n):
		sum += input[((n+1)*col)]
		
	if sum != goal:
		magic = False

#diag2		
if magic == True:
	sum = 0
	for col in xrange(n):
		sum += input[n*(col + 1) - (col + 1)]
		
	if sum != goal:
		magic = False	
		
print "\n",input, "is a magic square:", magic,"\n"