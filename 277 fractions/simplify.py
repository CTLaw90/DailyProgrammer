#DAILY PROGRAMMER 277 EASY
#SIMPLFYING FRACTIONS

def gcd(a, b):
	while b:
		a, b = b, a%b
	
	return a
	
x = int(raw_input('enter numerator: '))
y = int(raw_input('enter denominator: '	))
	
mygcd = gcd(x, y)
print x//mygcd, y//mygcd