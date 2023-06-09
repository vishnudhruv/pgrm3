class shape:
	def __init__(self,a):
		self.side1=a
		self.ar=0
	def area(self):
		pass
	def display(self):
		print("Area is ",self.ar)
class rectangle(shape):
	def __init__(self,a,b):
		shape.__init__(self,a)
		self.side2=b
	def area(self):
		self.ar=self.side1*self.side2
class square(shape):
	def __init__(self,a):
		shape.__init__(self,a)
	def area(self):
		self.ar=self.side1**2
l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
rect=rectangle(l,b)
rect.area()
rect.display()
sd=int(input("Enter the side of square : "))
sq=square(sd)
sq.area()
sq.display()



		