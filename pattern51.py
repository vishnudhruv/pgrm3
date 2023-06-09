n=int(input("Enter the number of lines : "))
for g in range(n,0,-1):
	for i in range(1,g+1):
		for j in range(n+1,0,-1):
			if j>i:
				print(" ",end=" ")
			else:
				print("*",end=" ")
		for k in range(2,i+1):
			print("*",end=" ")
		print(" ")

