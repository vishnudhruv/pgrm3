n=int(input("Enter the number of lines : "))
for i in range(1,n):
	for j in range(n,i-1,-1):
		print(i,end=" ")
	print()

	