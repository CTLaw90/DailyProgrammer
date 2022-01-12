#DAILYPROGRAMMER 157 INTERMEDIATE
#RUBIKS CUBE SIMULATOR

import numpy as np

class cube:
	def __init__(self):
		self.body = np.reshape((['*']*125),(5,5,5))
		self.body[0,:,:] = np.reshape((['w']*25),(5,5))
		self.body[4,:,:] = np.reshape((['y']*25),(5,5))
		self.body[:,0,:] = np.reshape((['r']*25),(5,5))
		self.body[:,4,:] = np.reshape((['o']*25),(5,5))
		self.body[:,:,0] = np.reshape((['g']*25),(5,5))
		self.body[:,:,4] = np.reshape((['b']*25),(5,5))
	
	def rotateSide(self, side, dir):
		if side == 'F':
			self.body[0,:,:] = np.rot90(self.body[0,:,:], dir) 
			self.body[1,:,:] = np.rot90(self.body[1,:,:], dir) 
		if side == 'B':
			self.body[3,:,:] = np.rot90(self.body[3,:,:], -dir) 
			self.body[4,:,:] = np.rot90(self.body[4,:,:], -dir)
		if side == 'U':
			self.body[:,0,:] = np.rot90(self.body[:,0,:], -dir) 
			self.body[:,1,:] = np.rot90(self.body[:,1,:], -dir)
		if side == 'D':
			self.body[:,3,:] = np.rot90(self.body[:,3,:], dir) 
			self.body[:,4,:] = np.rot90(self.body[:,4,:], dir)
		if side == 'L':
			self.body[:,:,0] = np.rot90(self.body[:,:,0], dir) 
			self.body[:,:,1] = np.rot90(self.body[:,:,1], dir)
		if side == 'R':
			self.body[:,:,3] = np.rot90(self.body[:,:,3], -dir) 
			self.body[:,:,4] = np.rot90(self.body[:,:,4], -dir)
			
	def printCube(self):
		
		# for i in xrange(5):
			# print self.body[i,:,:], '\n'
		
		print self.body[0,:,:][1:4,1:4]
		print '---------------------------------------------'	

def main():		
	a = cube()
	input = "U2 R' D2 R F L' U2 R"
	a.printCube()

	for item in input.split(' '):
		print item
		if len(item) == 1 and item in ['F','B','U','D','L','R']:
			a.rotateSide(item, -1)
		elif item[1] == '2':
			a.rotateSide(item[0], -1)
			a.rotateSide(item[0], -1)
		elif item[1] == "'":
			a.rotateSide(item[0], 1)
		else:
			print 'error'
			break
			
	a.printCube()
	
main()
