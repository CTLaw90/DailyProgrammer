#daily programmer 366
#tessellations

pattern = open('input.txt')
pattern = pattern.read()
pattern = pattern.split('\n')

rotation = int(pattern[0])
size = int(pattern[1])

x = []
for n in xrange(size):
	x.append(['']*size)

for i in xrange(size):
	for j in xrange(size):
		x[i][j] = pattern[i+2][j]
		
print x

def rot90():
	global x
	for i in xrange(size):
		for j in xrange(size):
			print i,j, x[i][j]
			x[size-1-i][j] = x[i][j]

rot90()			
print x			
