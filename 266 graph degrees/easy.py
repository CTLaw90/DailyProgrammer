#dailyprogrammer 266
#graph degrees

input_txt = open('challenge1.txt')
input = input_txt.read()
input = input.split('\n')

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		
	def addConnection(self, nbr, weight=0):
		self.connectedTo[nbr] = weight
		
	def getDegree(self):
		print "Node " + str(self.id) + " has a degree of: " + str(len(self.connectedTo.keys()))
		
	def getConnections(self):
		return self.connectedTo.keys()


class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVerts = 0
		
	def addVert(self, key):
		self.numVerts += 1
		newVert = Vertex(key)
		self.vertList[key] = newVert
		return newVert

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVert(f)
		if t not in self.vertList:
			nv = self.addVert(t)
		self.vertList[f].addConnection(self.vertList[t], cost)
		self.vertList[t].addConnection(self.vertList[f], cost)
		
G = Graph()

for i in range(1, int(input[0])+1):
	# create new vertex with id i
	G.addVert(i)

n = int(input[0])	
bonus = [[(0) for x in range(n)] for y in range(n)]
	
input.pop(0)	
i=[0,0]	
	
for j in input:
	#create new edge between nodes
	i[0],i[1] = j.split(' ')
	G.addEdge(int(i[0]),int(i[1]))
	
for node in G.vertList.keys():
	G.vertList[node].getDegree()
	for connection in G.vertList[node].getConnections():
		bonus[(node)-1][(connection.id)-1] = 1

for row in bonus:
	print row