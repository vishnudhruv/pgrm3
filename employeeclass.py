class employee:
	def read_data(self,ename,ecode,ebs):
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
		print("Name			: ",self.emp_name)
		print("Empcode		: ",self.emp_code)
		print("Basic salary	: ",self.emp_basic)
		print("DA			: ",self.emp_da)
		print("HRA			: ",self.emp_hra)
		print("PF			: ",self.emp_pf)
		print("Net salary	 	: ",self.emp_ns)
emp1=employee()
emp2=employee()
n1=input("Enter the name of first employee : ")
c1=input("Enter the code of first employee : ")
bs1=int(input("Enter the basic salary of first employee :"))
n2=input("Enter the name of second employee : ")
c2=input("Enter the code of second employee : ")
bs2=int(input("Enter the basic salary of second employee :"))
emp1.read_data(n1,c1,bs1)
emp2.read_data(n2,c2,bs2)
emp1.calculate()
emp2.calculate()
emp1.display()
emp2.display()





