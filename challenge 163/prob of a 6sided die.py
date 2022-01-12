#The Daily Programmer Challenge163 Easy
#Prob of a 6sided die

import random

Max_Roll = 1000000

Rolls = [0, 0, 0, 0, 0, 0]

for i in xrange(1, Max_Roll+1):
	side = random.randint(1, 6)
	Rolls[side-1] += 1
	
for s in Rolls:
	print (s/Max_Roll)