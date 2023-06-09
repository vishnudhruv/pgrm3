class bank:
	def __init__(self,name,acct_no):
		self.name=name
		self.acct_no=acct_no
		self.balance=0

	def display(self):
		print("ACCOUNT DETAILS")
		print("---------------")
		print("Account Holder:",self.name)
		print("Account Number:",self.acct_no)
		print()

	
	def deposit(self,deposit):
		self.dp=deposit
		self.balance=self.balance+self.dp
		print("Deposited Successfully")
		print()

	def withdraw(self,w):
		if w<self.balance:
			self.balance=self.balance-w
			print("Amount Withdrawed")
		else:
			print("Not Enough Balance!")

	def balance1(self):
		return self.balance

name=input("Enter the Account Holder Name:")
acct_no=input("Enter the Account Number:")
s=bank(name,acct_no)
s.display()
print("1.Deposit Money")
print("2.Withdraw Money")
print("3.View Balance")
print("4.Exit")
while(True):
	print()
	n=int(input("Enter the Choice:"))
	if n==1:
		deposit=int(input("Enter the Amount to Deposit:"))
		s.deposit(deposit)
	elif n==2:
		wdraw=int(input("Enter the Amount to Withdraw:"))
		s.withdraw(wdraw)
	elif n==3:
		print("Balance is:",s.balance1())
	elif n==4:
		print("Exiting!")
		break
	else:
		print("Wrong Choice!")




	