#pancake stack flip problem

input = '7 6 4 2 6 7 8 7'
stack = input.split(' ')
counter = 0


def flip(x):
	global stack, counter
	counter += 1
	print "FLIP " , counter , " : " , stack , " @INDEX ", x
	stack = stack[x::-1] + stack[x+1::]
	


t = True
while t == True:
	for i in xrange(len(stack)):
		if counter == 100:
			t = False
		max = None
		greater = None
		for j in xrange(i,len(stack)):
			if stack[i] > stack[j]:
				if max == None:
					max = j
				else:
					if stack[i] > stack[max]:
						max = j
		if max != None:
			flip(max)
			break
			
		if i == len(stack) - 1:
			t = False
			
print "TOTAL FLIPS ", counter , stack