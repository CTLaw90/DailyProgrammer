#Complex Numbers
import math

class Complex:
	def __init__(self, real, imag):
		self.r = float(real)
		self.i = float(imag)
		
	def __add__(self, other):
		return Complex(self.r + other.r, self.i + other.i)
		
	def __sub__(self, other):
		return Complex(self.r - other.r, self.i - other.i)
		
	def __mul__(self, other):
		return Complex(((self.r * other.r) - (self.i * other.i)),((self.i * other.r) + (self.r * other.i)))

	def __div__(self, other):
		num = self * other.GetConjugate()
		denom = other * other.GetConjugate()
		return Complex(1/denom.r, 0) * num

	def GetModulus(self):
		return math.sqrt((self.r)**2 + (self.i)**2)
		
	def GetConjugate(self):
		return Complex(self.r, self.i * -1)
		
	def GetArgument(self):
		return math.atan2(self.i, self.r)
		
	def ToString(self):
		print str(self.r) + " + " + str(self.i) + "i"
		
		
test1 = Complex(4, 2)
test2 = Complex(3, -1)



result = test1/test2
result.ToString()
