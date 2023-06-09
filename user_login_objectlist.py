class user:
	user_name=""
	password=[]
	def __init__(self,uname,pswd):
		self.user_name=uname
		self.password.append(pswd)
	def get_password(self):
		return self.password[-1]
	def is_correct(self,pwd):
		if pwd==get_password():
			return true
		else:
			return false
	def set_password(self,pwd):
		if pwd not in self.password:
			self.password.append(pwd)
		else:
			print("Cannot reset-old password!!!!")


					
