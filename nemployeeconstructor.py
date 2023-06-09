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
employee_list=[]
n=int(input("Enter the number of employees : "))
for i in range(0,n):
	nme=input("Enter the name of employee : ")
	c=input("Enter the code of employee : ")
	bs=int(input("Enter the basic salary of employee :"))
	emp=employee(nme,c,bs)
	emp.calculate()
	employee_list.append(emp)
for i in range(0,n):
	employee_list[i].display()






