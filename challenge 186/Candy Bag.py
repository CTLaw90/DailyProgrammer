#186 Candy Bag

raw_list = open('candy.txt')
candy_list = raw_list.read()
candy_list = candy_list.split('\n')

def Candy_Bag(list):
	contents = {}
	for item in list:
		if item in contents:
			contents[item] += 1
			
		else:
			contents[item] = 1
			
	print contents

print "You have: " + str(len(candy_list)) + " pieces"	
Candy_Bag(candy_list)