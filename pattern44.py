n=int(input("Enter the number : "))
k=1
for i in range(1,n+1):
	for j in range(1,i+1):
		print(k,end="\t")
		k=k+1
	print()