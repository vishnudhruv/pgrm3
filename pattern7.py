n=int(input("Enter the number of lines : "))
for i in range(1,n+1):
	for j in range(n,i-1,-1):
		print(j*2,end=" ")
	print()

	