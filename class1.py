class number:
		x=5
		def print_x(self):
			y=50
			print(y)
			print(self.x)
			self.x=self.x+10
		def another(self):
			#print(y)  #error
			print(self.x)
n=number()
print(n.x)	
m=number()
print(m.x)	
m.x=25
print(m.x)	
m.print_x()
print(m.x)	
print(n.x)	
n.print_x()
print(n.x)	
n.another()
m.another()





