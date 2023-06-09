n=int(input("Enter the no of lines : "))
k=1
for i in range(1,n+1):
	for j in range(1,i+1):
		if k%2==0:
			print("+",end=" ")
		else:
			print("*",end=" ")
		k+=1
	print()


