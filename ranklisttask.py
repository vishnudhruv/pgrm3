class student:
	def __init__(self,nme,r,m):
		self.name=nme
		self.rollno=r
		self.marks=m
		self.total=0
	def calculate(self):
		for i in range(5):
			self.total+=self.marks[i]
	def display(self):
		print("Name 			: ",self.name)
		print("Roll No			: ",self.rollno)
		for i in range(5):
			print(f"Mark for subject {i+1}	:",self.marks[i])
		print("Total marks 		: ",self.total)
		print("-----------------------")
student_list=[]
n=int(input("Enter the number of students : "))
for i in range(0,n):
	nme=input("Enter student name :")
	rno=int(input("Enter the roll no :"))
	m=[]
	print("Enter the marks for 5 subjects : ")
	for j in range(5):
		x=int(input())
		m.append(x)
	s=student(nme,rno,m)
	s.calculate()
	student_list.append(s)
for s in student_list:
	s.display()
for i in range(0,n-1):
	for j in range(i+1,n):
		if student_list[i].total<student_list[j].total:
			x=student_list[i]
			student_list[i]=student_list[j]
			student_list[j]=x
print("Rank\tName\tRollno\tTotal")
for i in range(0,n):
	print(i+1,"\t",student_list[i].name,"\t",student_list[i].rollno,"\t",student_list[i].total)