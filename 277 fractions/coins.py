#DAILY PROGRAMMER 277 INTERMEDIATE
#WEIGHTED COINS

input = ['a b left',
		'a c equal',]

coins = {}		
		
for line in input:
	item = line.split(' ')
	x = item[0]
	y = item[1]
	dir = item[2]
	print item, x, y, dir
	if x not in coins.keys():
		coins[x] = 1
	if y not in coins.keys():
		coins[y] = 1
	
	if dir == 'right':
		if coins[x] == coins[y]:
			coins[x] = coins[x]*.5
			
	if dir == 'left':
		if coins[x] == coins[y]:
			coins[y] = coins[y]*.5
			
	if dir == 'equal':
		if coins[x] < coins[y]:
			coins[y] = coins[x]
			
		elif coins[y] < coins[x]:
			coins[x] = coins[y]
	print coins.keys()
			
print coins
		