#Men, Trees, and BEARS

import random

##########VARIABLES#########

Tick = 0
			#[0][1] [2]
Sap = []	#[y, x, age]
Tree = []	#[y, x, age]
Elder = []	#[y, x, age]
Man = []	#[y, x] 
Bear = []	#[y, x]

Lumber = 0
Maw = 0

##########BOARD INITIALIZE#########

#N is the length of one side
N = 10 

#Creating an N x N matrix filled with 0
Board = [[0 for i in range(N)] for j in range(N)]


##########BOARD DRAW##########
def Draw_Board(Board):
	for lvl in range(N):
		print Board[lvl]
		
		
	
##########MOVEMENT#########
	
#find random empty space
def Find_Empty(board):
	done = False
	while not done:
		spot_X = random.randrange(0, N)
		spot_Y = random.randrange(0, N)	
		if board[spot_Y][spot_X] == 0:
			return [spot_Y, spot_X]
	
#find nearby empty space
def Find_Near_Empty(board, y, x):
	global N
	locs = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N:
				if board[y+i][x+j] == 0:
					locs.append([y+i, x+j])

	return locs
	
def Man_Move(board, y, x):
	#same as find empty space but we want to be able to 'move' onto trees as well
	global N
	locs = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N:
				if board[y+i][x+j] == 0:
					locs.append([y+i, x+j, 0])
				elif board[y+i][x+j] == 2:
					locs.append([y+i, x+j, 2])
				elif board[y+i][x+j] == 3:
					locs.append([y+i, x+j, 3])

	return locs
	
def Bear_Move(board, y, x):
	#same as find empty space but we want to be able to 'move' onto men as well
	global N
	locs = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N:
				if board[y+i][x+j] == 0:
					locs.append([y+i, x+j, 0])
				elif board[y+i][x+j] == 4:
					locs.append([y+i, x+j, 4])

	return locs
##########BOARD POPULATE##########
'''
KEY
0 == BLANK
1 == SAPLING
2 == TREE
3 == ELDER TREE
4 == LUMBERJACK
5 == BEAR
'''


#Tree populate
#We want 50% trees to start with

for tree in range((N**2)/2):
	loc = Find_Empty(Board)
	Board[loc[0]][loc[1]] = 2
	Tree.append([loc[0], loc[1], 0])
	
#Lumberjack populate
#We want 10% doods to start with #using 5% for time being

for dood in range((N**2)/20):
	loc = Find_Empty(Board)
	Board[loc[0]][loc[1]] = 4
	Man.append([loc[0], loc[1]])
	
#Bear populate
#We want 2% bears to start with

for bear in range((N**2)/50):
	loc = Find_Empty(Board)
	Board[loc[0]][loc[1]] = 5
	Bear.append([loc[0], loc[1]])

	
##########TICK##########
def Next_Tick():
	global Tick, Sap, Tree, Elder, Man, Bear, Lumber, Maw, Board
	Tick += 1
	
	loc = []
	
	#trees
	
	#grow new sapling from trees
	for tree in Tree:
		#want to grow 10% of the time
		if random.randrange(0,10) == 0:
			#find possible locations
			opt_locs = Find_Near_Empty(Board, tree[0], tree[1])
			#choose one, if any exist
			if len(opt_locs) > 0:
				loc = opt_locs[random.randrange(0, len(opt_locs))]
				#put sapling there
				Board[loc[0]][loc[1]] = 1
				Sap.append([loc[0], loc[1], 0])
		#age them all
		tree[2] += 1
		if tree[2] == 120:
			Board[tree[0]][tree[1]] = 3
			Elder.append([tree[0], tree[1], 0])
			Tree.remove(tree)
		
	#grow new spaling from elder tree, with higher occurance
	for eld in Elder:
		#want to grow 20% of the time
		if random.randrange(0,5) == 0:
			#find possible locations
			opt_locs = Find_Near_Empty(Board, eld[0], eld[1])
			#choose one, if any exist
			if len(opt_locs) > 0:
				loc = opt_locs[random.randrange(0, len(opt_locs))]
				#put sapling there
				Board[loc[0]][loc[1]] = 1
				Sap.append([loc[0], loc[1], 0])
		#age
		eld[2] += 1
		
	#age the saplings
	for sapl in Sap:
		sapl[2] += 1
		#if sapling is of age, turn into a tree
		if sapl[2] == 12:
			Board[sapl[0]][sapl[1]] = 2
			Tree.append([sapl[0], sapl[1], 0])
			Sap.remove(sapl)
	
	
	#men
	
	#move up to 3 times, or chop down tree
	for dood in Man:
		moves = 0
		find_tree = False
		while moves < 3 and not find_tree:
			opt_locs = Man_Move(Board, dood[0], dood[1])
			if len(opt_locs) > 0:
				loc = opt_locs[random.randrange(0, len(opt_locs))]
				if loc[2] == 2:
					Board[dood[0]][dood[1]] = 0
					Board[loc[0]][loc[1]] = 4
					dood[0] = loc[0]
					dood[1] = loc[1]
					
					for tree in Tree:
						if tree[0] == loc[0] and tree[1] == loc[1]:
							Tree.remove(tree)
					
					
					Lumber += 1
					find_tree = True
					
				if loc[2] == 3:
					Board[dood[0]][dood[1]] = 0
					Board[loc[0]][loc[1]] = 4
					dood[0] = loc[0]
					dood[1] = loc[1]
					
					for eld in Elder:
						if eld[0] == loc[0] and eld[1] == loc[1]:
							Elder.remove(eld)
					
					Lumber += 2
					find_tree = True
				
				else:
					Board[dood[0]][dood[1]] = 0
					Board[loc[0]][loc[1]] = 4
					dood[0] = loc[0]
					dood[1] = loc[1]
			moves += 1
	
	#bears
	
	for bear in Bear:
		moves = 0
		find_man = False
		while moves < 5 and not find_man:
			opt_locs = Bear_Move(Board, bear[0], bear[1])
			if len(opt_locs) > 0:
				loc = opt_locs[random.randrange(0, len(opt_locs))]
				if loc[2] == 4:
					Board[bear[0]][bear[1]] = 0
					Board[loc[0]][loc[1]] = 5
					bear[0] = loc[0]
					bear[1] = loc[1]
					
					for dood in Man:
						if dood[0] == loc[0] and dood[1] == loc[1]:
							Man.remove(dood)
					
					
					Maw += 1
					find_man = True
					
			moves += 1
			
	#year event		
	if Tick % 12 == 0:
		#hire/fire
		man_change = round(Lumber/10)
		if man_change < 0:
			for i in range(abs(int(man_change))):
				Man.pop()
				
		elif man_change > 0:
			for i in range(int(man_change)):
				loc = Find_Empty(Board)
				Board[loc[0]][loc[1]] = 4
				Man.append([loc[0], loc[1]])
		
		Lumber = 0
				
	
	
	print "\nMONTH: ", Tick
	print "MEN: ", len(Man)
	print "BEARS: ", len(Bear)
	print "LUMBER: ", Lumber
	print "MAW: ", Maw, "\n"
	
	
	
##########MAIN##########

for i in range(50):

	Next_Tick()
	Draw_Board(Board)
	
	print '\n-------------------------------------\n'


