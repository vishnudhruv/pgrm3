n=int(input("enter the maximum count : "))
for x in range(1,n+1):
	for i in range(n,x-1,-1):
		for j in range(n,i-1,-1):
			print(i,end=" ")
		print("")
	for i in range(x+1,n):
		for j in range(n,i-1,-1):
			print(i,end=" ")
		print("")
print(x)