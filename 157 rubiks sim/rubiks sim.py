#DAILYPROGRAMMER 157 INTERMEDIATE
#RUBIKS CUBE SIMULATOR

class side:
	def __init__(self, c):		#c = color
		self.face =	[	[c,c,c],
						[c,c,c],
						[c,c,c]		]
						
		self.left = None
		self.right = None
		self.up = None
		self.down = None
		self.leftEdge = None
		self.rightEdge = None
		self.upEdge = None
		self.downEdge = None
		
	def updateEdge(self):
		self.leftEdge = (self.face[0][0],self.face[1][0],self.face[2][0])
		self.rightEdge = (self.face[0][2],self.face[1][2],self.face[2][2])
		self.upEdge = (self.face[0])
		self.downEdge = (self.face[2])
		
	def setAdjacent(self, l,r,u,d):
		self.left = l
		self.right = r
		self.up = u 
		self.down = d
		
	def testSetFace(self, array):
		self.face = array

class cube:
	def __init__(self):
		self.f = side('w')
		self.b = side('y')
		self.r = side('g')
		self.l = side('b')
		self.u = side('r')	
		self.d = side('o')
		self.sides = {	'f': self.f,
						'b': self.b,
						'r': self.r,
						'l': self.l,
						'u': self.u,
						'd': self.d		}
		
		self.f.setAdjacent(self.l,self.r,self.u,self.d)
		self.b.setAdjacent(self.r,self.l,self.u,self.d)
		self.r.setAdjacent(self.f,self.b,self.u,self.d)
		self.l.setAdjacent(self.b,self.f,self.u,self.d)
		self.u.setAdjacent(self.l,self.r,self.b,self.f)
		self.d.setAdjacent(self.l,self.r,self.f,self.b)
		
		self.setEdges()
		
	def setEdges(self):
		for i in self.sides.keys():
			self.sides[i].updateEdge()
		
	def testTurn(self):
		self.testSide = side('')
		self.testSide.testSetFace([	[1,2,3],[4,5,6],[7,8,9]	])
		print self.testSide.face
		self.turn90(self.testSide)
		print self.testSide.face
									
	def turn90(self, mainSide):
		"""
		[a,b,c]				[g,d,a]
		[d,e,f]		->		[h,e,b]
		[g,h,i]				[i,f,c]
		"""
		x = mainSide.face
		a,b,c,d = mainSide.left.face,mainSide.up.face,mainSide.right.face,mainSide.down.face
		x[0][0],x[0][1],x[0][2],x[1][0],x[1][2],x[2][0],x[2][1],x[2][2] = x[2][0],x[1][0],x[0][0],x[2][1],x[0][1],x[2][2],x[1][2],x[0][2]
		a[2][2],a[1][2],a[0][2],b[2][0],b[2][1],b[2][2],c[0][0],c[1][0],c[2][0],d[0][2],d[0][1],d[0][0] = d[0][2],d[0][1],d[0][0],a[2][2],a[1][2],a[0][2],b[2][0],b[2][1],b[2][2],c[0][0],c[1][0],c[2][0]
		self.setEdges()
	
	
	def turn90p(self, mainSide):
		x = mainSide.face
		a,b,c,d = mainSide.left.face,mainSide.up.face,mainSide.right.face,mainSide.down.face
		x[0][0],x[0][1],x[0][2],x[1][0],x[1][2],x[2][0],x[2][1],x[2][2] = x[2][0],x[1][0],x[0][0],x[2][1],x[0][1],x[2][2],x[1][2],x[0][2]
		a[2][2],a[1][2],a[0][2],b[2][0],b[2][1],b[2][2],c[0][0],c[1][0],c[2][0],d[0][2],d[0][1],d[0][0] = b[2][0],b[2][1],b[2][2],c[0][0],c[1][0],c[2][0],d[0][2],d[0][1],d[0][0],a[2][2],a[1][2],a[0][2],

def main():
	myCube = cube()
	instructions = 'F'
	instructions = instructions.lower()
	instructions = instructions.split(' ')
	printCube(myCube)
	for item in instructions:
		print item
		myCube.turn90(myCube.sides[item])
		printCube(myCube)

		
def printCube(myCube):
	for key in myCube.sides.keys():
		print key, myCube.sides[key].face
		print myCube.sides[key].leftEdge
	print '----------------------------------------'
	
main()