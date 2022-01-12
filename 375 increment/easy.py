#dailyprogrammer 375

input = 998

def increment(x):
	y = 0
	z = 0
	if x < 10:
		y = x+1
		return(y)
		
	else:
		y = (x%10) + 1
		z = increment(x/10) * 10
		
	if y == 10:
		z = (z)*10
		
	return(y+z)
	
print(increment(input))