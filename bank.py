class  bank_account:
	def ___init__(self,acno,bal):
		self.accountno=acno
		self.balance=bal
	def deposit(self,amt):
		self.balance=self.balance+amt
		print("Your current balance is ",self.balance)
	def withdrawl(self,amt):
		if amt<self.balance:
			self.balance=self.balance-amt
			print("Your current balance is ",self.balance)
		else:
			print("No sufficient balance")