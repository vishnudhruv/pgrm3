n=int(input("Enter the number of lines : "))
for i in range(1,n+1):
	for m in range(0,2):
		for j in range(n,0,-1):
			if j>i:
				print(" "*3,end=" ")
			else:
				print("*"*3,end=" ")
		for k in range(1,i+1):
			print("*"*3,end=" ")
		print(" ")
