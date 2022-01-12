#dailyprogrammer 379
#progressive taxation

import sys


def findtax(income):
	bracket = [	(10000, 	0.0),
				(30000,		0.1),
				(100000,	0.25),
				(10000000,	0.4)]
	
	tax = 0.0
	
	for i in range(len(bracket)):
		if i>0:
			if (income > bracket[i][0]):
				tax += ((bracket[i][0] - bracket[i-1][0])*(bracket[i][1]))
			else:
				tax += ((income - bracket[i-1][0])*(bracket[i][1]))
		else:
			if (income > bracket[i][0]):
				tax += ((bracket[i][0])*(bracket[i][1]))
			else:
				tax += ((income)*(bracket[i][1]))		
		
		if income < bracket[i][0]:
			return(tax)
	return(tax)
	
print(findtax(int(sys.argv[1])))