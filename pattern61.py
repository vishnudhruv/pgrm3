n=int(input("Enter the number of lines : "))
for i in range(1,n):
	for j in range(n,1,-1):
			print(" ",end=" ")
	for k in range(1,i+1):
		if k==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print(" ")
for i in range(1,(2*n)):
	print("*",end= " ")
print(" ")
for i in range(1,n):
	for j in range(1,n):
			print(" ",end=" ")
	for k in range(n-1,i-1,-1):
		if k==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print(" ")
