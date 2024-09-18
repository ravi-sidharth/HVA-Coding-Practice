array = list(map(int,input("Enter the array: ").split()))

sum=0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        sum+=abs(array[i]-array[j])
print(sum)