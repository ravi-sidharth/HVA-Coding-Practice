n = list(map(int,input("Enter the array: ").split()))

len = len(n)
sum=0
for i in range(len):
    for j in range(len-i+1):
        for k in range(i,i+j):
            sum+=n[k]
print(sum)