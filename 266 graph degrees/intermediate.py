#dailyprogrammer 266
#graph radius and diameter

#for this particular problem I will be using a BFS to find the eccentricity of any particular vertex

import sys

input_txt = open('data.txt')
input = input_txt.read()
input = input.split('\n')

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		self.dist = -1
		self.parent = None
		
		
	def addConnection(self, nbr, weight=1):   #setting base weight equal to one so we can have a base eccentricity
		self.connectedTo[nbr] = weight		#note that the keys in this dict are the vertices themselves and NOT the ids, opposed to the dict for the graph
		
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
		# self.vertList[t].addConnection(self.vertList[f], cost)   graph is now directed so we only want one direction
		
def Eccentricity(graph, root):
	for n in graph.vertList:
		vert = graph.vertList[n]
		vert.dist = -1
		vert.parent = None
		
	Q = []
	
	Q.append(root)
	root.dist = 0
	
	while Q:
		current = Q.pop(0)
		
		for adj in current.connectedTo:
			if adj.dist == -1:
				adj.dist = current.dist + 1
				adj.parent = current
				Q.append(adj)
	
	ecc = 0
	for n in graph.vertList:
		vert = graph.vertList[n]
		if (vert.dist > ecc):
			ecc = vert.dist
			
	return ecc

n = int(input[0])			
G = Graph()

for i in range(1, n+1):
	# create new vertex with id i
	G.addVert(i)

# bonus = [[(0) for x in range(n)] for y in range(n)]   not using bonus graph
	
input.pop(0)	
i=[0,0]	
	
for j in input:
	#create new edge between nodes
	i[0],i[1] = j.split(' ')
	G.addEdge(int(i[0]),int(i[1]))


radG = n
diaG = -1	
for node in G.vertList:
	x = Eccentricity(G, G.vertList[node])
	if x > diaG:
		diaG = x
		
	if (x < radG) and (x != 0):
		radG = x
	
print "radius: ", radG
print "diameter: ", diaG