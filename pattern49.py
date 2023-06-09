n=int(input("Enter the count : "))
for k in range(n,0,-1):
	for i in range(1,k+1):
		for j in range(n,0,-1):
			if j>i:
				print(" ",end=" ")
			else:
				print(j,end=" ")
		print()
	for i in range(k-1,1,-1):
		for j in range(n,0,-1):
			if j>i:
				print(" ",end=" ")
			else:
				print(j,end=" ")
		print()
for i in range(1,n):
	print(" ",end=" ")
print('1')
