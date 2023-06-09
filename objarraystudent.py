class student:
	def __init__(self,nme,a,b,c):
		self.name=nme
		self.m1=a
		self.m2=b
		self.m3=c
		self.total=0
	def calculate(self):
		self.total=self.m1+self.m2+self.m3
	def display(self):
		print("Name 		: ",self.name)
		print("Physics 		: ",self.m1)
		print("Chemistry		: ",self.m2)
		print("Mathematics 	: ",self.m3)
		print("Total marks 	: ",self.total)
		print("-----------------------")
student_list=[]
n=int(input("Enter the number of students : "))
for i in range(0,n):
	nme=input("Enter student name :")
	x=int(input("Enter the marks for Physics : "))
	y=int(input("Enter the marks for Chemistry : "))
	z=int(input("Enter the marks for Mathematics : "))
	s=student(nme,x,y,z)
	s.calculate()
	student_list.append(s)
for s in student_list:
	s.display()
