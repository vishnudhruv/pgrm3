def reverse(n):
	rev=0
	while n!=0:
		d=n%10
		rev=(rev*10)+d
		n=n//10
	return rev
no=int(input("Enter the number : "))
print("Reverse is ",reverse(no))
	