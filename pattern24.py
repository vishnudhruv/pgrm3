n=int(input("Enter the count : "))
for i in range(1,n+1):
	for j in range(n,i-1,-1):
		print(i, end=" ")
	print()
for i in range(n-1,0,-1):
	for j in range(n,i-1,-1):
		print(i, end=" ")
	print()

