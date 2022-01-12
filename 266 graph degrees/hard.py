#dailyprogrammer 266
#maximal cliques

#for this solution I will be using the bron-kerbosch w/ pivot algorithm to find the maximal cliques of the input graph
#could be cleaned up a lot by using the set type instead of sticking with lists for R P and X

import sys

input_txt = open('harddata.txt')
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
		return len(self.connectedTo.keys())
		
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
		
	def getHighestDegree(self, opt):
		if len(opt) == 1:
			return opt[0]
	
		max = [0,0]
		for i in opt:
			x = self.vertList[i].getDegree()
			if x > max[1]:
				max = [i,x]

		return max[0]
		
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
	
def BronKerbosch(R, P, X):

	if not P and not X:
		global maxClique
		if len(R) > len(maxClique):
			maxClique = R
		return
		
	u = G.getHighestDegree(P+X)
	
	notConnected = G.vertList.keys()
	for c in G.vertList[u].connectedTo.keys():
		notConnected.remove(c.id)
	
	checkThese = []
	for elm in P:
		if elm in notConnected:
			checkThese.append(elm)
	
	for v in checkThese:
		neig = list(i.id for i in list(G.vertList[v].getConnections()))
		neigP = []
		neigX = []
		for i in neig:
			if P:
				if i in P:
					neigP.append(i)
			if X:
				if i in X:
					neigX.append(i)
		BronKerbosch(R + [v], neigP, neigX)
		# if P:
			# P = P.remove(v)
		X = X + [v]
	 
		
n = int(input[0])			
G = Graph()

maxClique = []

for i in range(1, n+1):
	# create new vertex with id i
	G.addVert(i)

	
input.pop(0)	
i=[0,0]	
	
for j in input:
	#create new edge between nodes
	i[0],i[1] = j.split(' ')
	G.addEdge(int(i[0]),int(i[1]))		#graph is undirected so we create and edge both ways
	G.addEdge(int(i[1]),int(i[0]))


BronKerbosch([], G.vertList.keys(), [])

print maxClique