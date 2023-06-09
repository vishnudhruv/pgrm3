class student:
	def __init__(self,nm,ag):
		self.name=nm
		self.age=ag
	def print_details(self):
		print("Name : ",self.name)
		print("Age : ",self.age)
student1=student("Lijo",21)
student2=student("Queen",23)
student1.print_details()
student2.print_details()