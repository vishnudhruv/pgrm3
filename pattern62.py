n=int(input("Enter the number of lines : "))
for i in range(n,0,-1):
	for j in range(1,n+1):
		if j<i:
			print(" ",end=" ")
		else:
			print(j,end=" ")
	for k in range(n-1,i-1,-1):
			print(k,end=" ")
	print(" ")
for i in range(2,n+1):
	for j in range(1,n+1):
		if j<i:
			print(" ",end=" ")
		else:
			print(j,end=" ")
	for k in range(n-1,i-1,-1):
			print(k,end=" ")
	print(" ")



