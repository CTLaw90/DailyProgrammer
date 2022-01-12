#Challenge 193 
#Warehouse

import math

class Warehouse:
	def __init__(self, vol):
		self.v = float(vol)
		
	def CubeDim(self):
		cuberoot = self.v ** (1/3.0)
		print "Height: " + str(cuberoot) + ", Width: " + str(cuberoot) + ", Length: " + str(cuberoot)
		
	def BallDim(self):
		cuberoot = self.v ** (1/3.0)
		radius = ((self.v/(cuberoot * math.pi)) ** (1/2.0))
		print "Height: " + str(cuberoot) + ", Radius: " + str(radius)
		
	def SphereDim(self):
		radius = ((self.v/(3 * math.pi)) ** (1/2.0))
		print "Radius: " + str(radius)
		
	def ConeDim(self):
		height = ((self.v ** (1/3.0)) ** 2)
		radius = (((3 * self.v)/(math.pi * height)) ** (1/2.0))
		print "Height: " + str(height) + ", Radius: " + str(radius)
		

def main():
	Volume = 42
	test = Warehouse(Volume)
	test.CubeDim()
	test.BallDim()
	test.SphereDim()
	test.ConeDim()
	
main()