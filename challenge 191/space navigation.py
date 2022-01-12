#daily programmer challenge 191 
#space navigation

import random

'''
0 for empty space
1 for asteroid
2 for gravity
5 for probe
9 for path
'''


#map generation
N = 10 

Probe_Loc[0] = start_x
Probe_Loc[1] = start_y


def map_gen():
	global N, Probe_Loc

	# create and NxN board filled with '0'
	Board = [[0 for i in range(N)] for j in range(N)]
	
	# populate board with "A" asteroids and "G" gravity wells
	for asteroid in range(int((N**2) * 0.3)):
		loc = Find_Empty(Board)
		Board[loc[0]][loc[1]] = 1
		
	for well in range(int((N**2) * 0.1)):
		loc = Find_Empty(Board)
		Board[loc[0]][loc[1]] = 2

	Board[start_x][start_y] = 5
		
	return Board

		
#find random empty space
def Find_Empty(board):
	done = False
	while not done:
		spot_X = random.randrange(0, N)
		spot_Y = random.randrange(0, N)	
		if board[spot_Y][spot_X] == 0:
			return [spot_Y, spot_X]
			
def Find_Near_Empty(board, y, x):
	global N
	locs = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N:
				if board[y+i][x+j] == 0:
					locs.append([y+i, x+j])

	return locs
		


		
def Draw_Board(Board):
	for lvl in range(N):
		print Board[lvl]
		
def Move_Probe(Board, x, y):
	
		
Draw_Board(map_gen(N))