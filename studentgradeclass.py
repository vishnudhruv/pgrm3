class student:
	def __init__(self,nme,r,a,b,c):
		self.name=nme
		self.rollno=r
		self.m1=a
		self.m2=b
		self.m3=c
		self.total=0
	def calculate(self):
		self.total=self.m1+self.m2+self.m3
	def check_grade(self):
		self.per=int((self.m1+self.m2+self.m3)*100/300)
		if self.m1>=50 and self.m2>=50 and self.m3>=50:
			if self.per>=90:
				self.grade="A+"
			elif self.per>=80:
				self.grade="A"
			elif self.per>=70:
				self.grade="B+"
			elif self.per>=60:
				self.grade="B"
			else:
				self.grade="C"
		else:
			self.grade="Failed"
	def display(self):
		print("Name 		: ",self.name)
		print("Roll No		: ",self.rollno)
		print("Physics 	: ",self.m1)
		print("Chemistry	: ",self.m2)
		print("Mathematics 	: ",self.m3)
		print("Total marks 	: ",self.total)
		print("Percentage 	: ",self.per)
		print("Grade	 	: ",self.grade)
		print("-----------------------")
student_list=[]
n=int(input("Enter the number of students : "))
for i in range(0,n):
	nme=input("Enter student name :")
	rno=int(input("Enter the roll no :"))
	x=int(input("Enter the marks for Physics : "))
	y=int(input("Enter the marks for Chemistry : "))
	z=int(input("Enter the marks for Mathematics : "))
	s=student(nme,rno,x,y,z)
	s.calculate()
	s.check_grade()
	student_list.append(s)
for s in student_list:
	s.display()
print("Name\tRollno\tTotal\tPercentage\tGrade")
for i in range(0,n):
	print(student_list[i].name,"\t",student_list[i].rollno,"\t",student_list[i].total,"\t",student_list[i].per,"\t\t",student_list[i].grade)