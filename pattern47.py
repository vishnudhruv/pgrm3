n=int(input("Enter the number of lines : "))
for i in range(1,n+1):
	for j in range(n,0,-1):
		if j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(1,i+1):
		if j==i:
			print("*",end=" ")
	print(" ")

for i in range(2,n+1):
	for j in range(1,n+1):
		if j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(n,i-1,-1):
		if j==i:
			print("*",end=" ")
	print(" ")
