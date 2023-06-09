class employee:
	def __init__(self,ename,ecode,ebs):
		self.emp_name=ename
		self.emp_code=ecode
		self.emp_basic=ebs
	def calculate(self):
		if self.emp_basic<10000:
			self.emp_da=self.emp_basic*0.2
			self.emp_hra=self.emp_basic*0.25
			self.emp_pf=self.emp_basic*0.05
		else:
			self.emp_da=self.emp_basic*0.1
			self.emp_hra=self.emp_basic*0.15
			self.emp_pf=self.emp_basic*0.03
		self.emp_ns=self.emp_basic+self.emp_da+self.emp_hra-self.emp_pf
	def display(self):
		print("Name	: ",self.emp_name)
		print("Empcode		: ",self.emp_code)
		print("Basic salary	: ",self.emp_basic)
		print("DA		: ",self.emp_da)
		print("HRA	: ",self.emp_hra)
		print("PF		: ",self.emp_pf)
		print("Net salary	: ",self.emp_ns)
class teacher(employee):
	def __init__(self,enm,ecd,ebs,dept):
		employee.__init__(self,enm,ecd,ebs)
		self.department=dept
		self.student=[]
	def mark_attendance(self,n):
		self.count=n
		print("Enter the attendance rollno wise(1-present/0-absent)")
		for i in range(0,n):
			att=int(input())
			self.student.append(att)
	def display_attendance(self):
		print("List of present students ")
		for i in range(0,self.count):
			if self.student[i]==1:
				print(i+1)
		print("List of absent students ")
		for i in range(0,self.count):
			if self.student[i]==0:
				print(i+1)
	def display(self):
		print("Name	: ",self.emp_name)
		print("Empcode		: ",self.emp_code)
		print("Department		: ",self.department)
		print("Basic salary	: ",self.emp_basic)
		print("DA		: ",self.emp_da)
		print("HRA	: ",self.emp_hra)
		print("PF		: ",self.emp_pf)
		print("Net salary	: ",self.emp_ns)
teacher_list=[]
m=int(input("Enter the number of teachers : "))
for i in range(0,m):
	nme=input("Enter the name of teacher : ")
	c=input("Enter the code of teacher : ")
	bs=int(input("Enter the basic salary of teacher :"))
	dept=input("Enter the department of the teacher : ")
	no=int(input("Enter the number of students : "))
	tchr=teacher(nme,c,bs,dept)
	tchr.mark_attendance(no)
	tchr.calculate()
	teacher_list.append(tchr)  
for i in range(0,m):
	print("--------------------------------------")
	teacher_list[i].display()
	teacher_list[i].display_attendance()






