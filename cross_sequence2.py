n = int(input('Enter the value of n: '))
for i in range(1,2*n):
	for k in range(1,n+1): 
		for j in range(1,2*n):
			if i==j or i+j==2*n:
				print("*", end=" ")
			elif j>i and i+j<2*n:
				print("*",end=" ")
			elif i+j>2*n and j<i:
				print("*",end=" ")
			else:
				print(" ", end=" ")
	print()