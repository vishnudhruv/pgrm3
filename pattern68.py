letter=input("Enter the word : ")
n=len(letter)
for i in range(1,n+1):
	m=0
	for j in range(n,0,-1):
		if j>i:
			print(" ",end=" ")
		else:
			print(letter[m],end=" ")
			m+=1
	m-=2
	for k in range(1,i):
		print(letter[m],end=" ")
		m-=1
	print(" ")

for i in range(2,n+1):
	m=0
	for j in range(1,n+1):
		if j<i:
			print(" ",end=" ")
		else:
			print(letter[m],end=" ")
			m+=1
	m-=2
	for k in range(n,i,-1):
		print(letter[m],end=" ")
		m-=1
	print(" ")








