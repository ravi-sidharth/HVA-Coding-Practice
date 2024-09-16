n = list(map(int,input("Enter the array: ").split()))
length = len(n)

for i in range(length):
    for j in range(length-i+1):
        for k in range(i,i+j):
            print(n[k],end=" ")
        print()
