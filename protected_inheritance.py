# program to illustrate protected
# data members in a class


# super class
class Shape:
	
	# constructor
	def get_data(self, length, breadth):
		self._length = length
		self._breadth = breadth
		
	# public member function
	def displaySides(self):

		# accessing protected data members
		print("Length: ", self._length)
		print("Breadth: ", self._breadth)


# derived class
class Rectangle(Shape):


	# public member function
	def calculateArea(self):
					
		# accessing protected data members of super class
		print("Area: ", self._length * self._breadth)
					

# creating objects of the
# derived class		
obj = Rectangle()
obj.get_data(80,50)
# calling derived member
# functions of the class
obj.displaySides()

# calling public member
# functions of the class
obj.calculateArea()

obj1=Rectangle()
obj1._length=20
obj1._breadth=10
obj1.displaySides()
obj1.calculateArea()
