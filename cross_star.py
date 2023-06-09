n = int(input('Enter the value of n: '))
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or i+j==2*n or i==n or j==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()