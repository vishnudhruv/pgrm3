n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
	k=1
	for j in range(1,n+1):
		if j<i:
			print(" ",end=" ")
		else:
			print(k,end=" ")
			k+=1
	print()
