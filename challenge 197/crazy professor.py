#Crazy Professor
#Daily programmer 197 Hard

def sieve(x):
	a = [True] * x
	a[0] = False
	a[1] = False
	
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, x, i):
				a[n] = False
	
	
test_this = sieve(20)
sum = 0
for i in test_this:
	sum += i
		
