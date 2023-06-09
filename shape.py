class shape:
	def __init__(self,prm):
		self.parameter=prm
		self.ar=0
	def area(self):
		print("Area :",self.ar)
class circle(shape):
	def __init__(self,prm):
		shape.__init__(self,prm)
	def area(self):
		self.ar=3.14*self.parameter**2
		print("Area : ",self.ar)
class square(shape):
	def __init__(self,prm):
		shape.__init__(self,prm)
	def area(self):
		self.ar=self.parameter**2
		print("Area : ",self.ar)
cr=circle(10)
cr.area()
sq=square(10)
sq.area()


