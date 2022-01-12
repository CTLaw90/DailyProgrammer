#part one of challenge 265
#perms
from copy import deepcopy

perms = []
n = 7

def permute(x, rem):
	if len(rem) == 1:
		global perms
		perms.append(x+rem)
		return
		
	for i in rem:
		newrem = deepcopy(rem)
		newrem.remove(i)
		permute((x+[i]), newrem)
		
start = []
for i in range(n):
	start.append(i)

permute([],start)

print perms[3239]