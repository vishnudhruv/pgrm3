n = int(input('Enter the value of n: '))
for i in range(1,2*n):
	for j in range(1,2*n):
		if i==j or i+j==2*n:
			print(j,end=" ")
		elif j==n:
			print(i,end=" ")
		elif i==n:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()