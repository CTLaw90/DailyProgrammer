#Daily Programmer Challenge158 Easy
#The Torn Number

Num_Len = 4

def Check_Torn(numset):		#going to baby mode this by making it just assume Num_Len is 4 here
	R_Num = 10*numset[0] + numset[1]
	L_Num = 10*numset[2] + numset[3]
	W_Num = 1000*numset[0] + 100*numset[1] + 10*numset[2] + numset[3]

	# print R_Num, L_Num
	
	Sum_Num = R_Num + L_Num
	if Sum_Num**2 == W_Num:
		print 'TORN NUMBER - ', W_Num

def Dig_Lvl(numset, iter):
	for x in xrange(0,10):
		if x not in numset:
			numset.append(x)
			
			# print 'hi!', numset, iter		
			
			if iter < Num_Len:
				Dig_Lvl(numset, iter+1)
			
			if iter == Num_Len:
				Check_Torn(numset)
			
			# print 'bye!', numset, iter
			
			numset.remove(x)
		
Dig_Lvl([], 1)
