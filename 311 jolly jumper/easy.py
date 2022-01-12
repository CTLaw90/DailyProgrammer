#daily programmer 311 easy
#jolly jumper

x = [8,1,6,-1,8,9,5,2,7]
n = len(x)

jolly = True
absdiffs = []
for i in range(n-1):
	absdiffs.append(abs(x[i] - x[i+1]))
	
for j in range(1,n):
	if j not in absdiffs:
		jolly = False

print "x:", x
print "n:", n		
print "absdiffs:", absdiffs
print jolly