#daily programmer 326 easy
#tetromino pieces

from random import shuffle
from copy import deepcopy

original = ["o", "i", "s", "z", "l", "j", "t"]

bag = []
line = []

while len(line) < 50:
	if bag == []:
		bag = deepcopy(original)
		shuffle(bag)
		
	line.append(bag.pop())
	
print "".join(line)