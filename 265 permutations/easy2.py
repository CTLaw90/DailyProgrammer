#part one of challenge 265
#perms

#using a factorial numbering system to find perm numbers of large items

from math import factorial

x = [25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,35,32,36,34,39,29,27,33,26,37,40,30,31,41,28,38]
n = 0

def permX(n):		#use this if you know n and want the factorial representation
	global x		#x will also be reversed so watch for that
	i = 1
	while n > factorial(i):
		i += 1
	
	print i
	for base in range(1, i+1):
		# print base, n, x
		rem = n%base
		x.append(int(rem))
		n = n//base
		
	x = x[::-1]
		
def permN(x):		#use this if you have the factorial representation and need the base 10 number
	i = len(x)
	n = 0
	for base in range(i):
		n += (x.pop() * factorial(base))
		
	return n

# permX(n)
n = permN(x)

print n, x