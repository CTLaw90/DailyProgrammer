#part one of challenge 265
#combs
from copy import deepcopy

perms = []
n = 9	#first x numbers
m = 4	#combs this big
def permute(x, rem):
	global m
	if len(x) == m:
		global perms
		perms.append(x)
		return
		
	for i in rem:
		if not x or (i > x[-1]):
			newrem = deepcopy(rem)
			newrem.remove(i)
			permute((x+[i]), newrem)
		
start = []
for i in range(n):
	start.append(i)

permute([],start)

print perms[111]