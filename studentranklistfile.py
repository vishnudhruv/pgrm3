import pickle
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
	def display(self):
		print("Name 		: ",self.name)
		print("Roll No		: ",self.rollno)
		print("Physics 	: ",self.m1)
		print("Chemistry	: ",self.m2)
		print("Mathematics 	: ",self.m3)
		print("Total marks 	: ",self.total)
		print("-----------------------")
student_list=[]
f=open("Rank","wb")
n=int(input("Enter the number of students : "))
for i in range(0,n):
	nme=input("Enter student name :")
	rno=int(input("Enter the roll no :"))
	x=int(input("Enter the marks for Physics : "))
	y=int(input("Enter the marks for Chemistry : "))
	z=int(input("Enter the marks for Mathematics : "))
	s=student(nme,rno,x,y,z)
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
for i in range(0,n):
	pickle.dump(student_list[i],f)
f=open("Rank","rb")
print("Rank\tName\tRollno\tTotal")
for i in range(0,n):
	stud=pickle.load(f)
	print(i+1,"\t",stud.name,"\t",stud.rollno,"\t",stud.total)