n=int(input("Enter the number of lines : "))
for i in range(n,0,-1):
	for j in range(n,0,-1):
		if j>i:
			print(" ",end=" ")
		else:
			print(j,end=" ")
	for k in range(2,i+1):
			print(k,end=" ")
	print(" ")



