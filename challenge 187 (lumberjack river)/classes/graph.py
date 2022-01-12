#Graph

#includes dfsGraph class object

import sys

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		self.color = 'white'
		self.dist = sys.maxsize
		self.pred = None
		self.disc = 0
		self.fin = 0
		
	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight
		
	def setWeight(self, nbr, weight):
		self.connectedTo[nbr] = weight
		
	def setColor(self, color):
		self.color = color
		
	def setDistance(self, d):
		self.dist = d
		
	def setPred(self, p):
		self.pred = p
		
	def setDiscover(self, dtime):
		self.disc = dtime
		
	def setFinish(self, fin):
		self.fin = fin
		
	def getFinish(self):
		return self.fin
		
	def getDiscover(self, dtime):	
		return self.disc
		
	def getPred(self):
		return self.pred
		
	def getDistance(self):
		return self.dist
		
	def getColor(self):
		return self.color
	
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
		
	def getConnections(self):
		return self.connectedTo.keys()
		
	def getId(self):
		return self.id
		
	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
		
	def addVertex(self, key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	
	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
			
	def __contains__(self, n):
		return n in self.vertList
		
	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)
		
	def getVertices(self):
		return self.vertList.keys()
		
	def __iter__(self):
		return iter(self.vertList.values())
		
		
class dfsGraph(Graph):
	def __init__(self):
		super().__init__()
		self.time = 0
		
	def dfs(self):
		for avert in self:
			avert.setColor('white')
			avert.setPred(-1)
		for avert in self:
			if avert.getColor == 'white':
				self.dfsVisit(avert)
				
	def dfsVisit(self, vert):
		vert.setColor('gray')
		self.time += 1
		vert.setDiscover(self.time)
		for nextVert in vert.getConnections():
			if nextVert.getColor() == 'white':
				nextVert.setPred(vert)
				self.dfsVisit(nextVert)
		vert.setColor('black')
		self.time += 1
		vert.setFinish(self.time)