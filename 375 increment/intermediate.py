#dailyprogrammer 375
#card flip

from copy import deepcopy
import sys

input = '100001100101000'
input = list(input)

def flip(cards, i):
	cards[i] = '.'
	if i > 0:
		if cards[i-1] != '.':
			cards[i-1] = str((int(cards[i-1]) + 1) % 2)
	if i < len(cards)-1:
		if cards[i+1] != '.':
			cards[i+1] = str((int(cards[i+1]) + 1) % 2)
	return(cards)
	
def findSol(cards, sol):
	a = deepcopy(cards)
	if ('0' not in cards) and ('1' not in cards):
		return sol
		
	for i in range(len(cards)):
		if cards[i] == '1':
			return findSol(flip(a, i), sol+[i])
			
	return('No Solution')

for i in range(1, len(sys.argv)):
	a = sys.argv[i]
	a = list(a)
	print(findSol(a, []))