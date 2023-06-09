class user:
	password=[]
	def __init__(self,pswd):
		self.password.append(pswd)
	def get_password(self):
		return self.password[-1]
	def is_correct(self,pwd):
		if pwd==self.get_password():
			return True
		else:
			return False
	def set_password(self,pwd):
		if pwd not in self.password:
			self.password.append(pwd)
			print("Password reset successfully!!!")
		else:
			print("Cannot reset-old password!!!!")
pwd=input("Enter a password :")
u=user(pwd)
print("1. Login")
print("2. Reset Password")
print("3. Exit")
while(1):
	choice=int(input("Enter your choice : "))
	if choice==1:
		pwd=input("Enter your current password : ")
		if u.is_correct(pwd):
			print("Logged in successfully")
		else:
			print("Invalid password!!!")
	elif choice==2:
		pwd=input("Enter a new password : ")
		u.set_password(pwd)
	elif choice==3:
		print("Exiting!!!")
		break
	else:
		print("Invalid choice!!!!")
		
		
		
	
	

					
