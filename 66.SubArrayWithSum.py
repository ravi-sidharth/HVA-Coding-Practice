array = list(map(int,input("Enter the array: ").split()))
targetSum=int(input("Enter the target sum: "))

# 3 6 2 1 7
# 10

#output 2 1 7
sum=0
start=0
count=0
for i in range(len(array)):
    for j in range(i,len(array)):
        sum+=array[j]
        if targetSum>=sum:
            count+=1
            start=i

        else:
            break
    
    if targetSum==sum:
        break 
    sum=0
    count=0

print(start)
print(count)
for k in range (start, start+count):
    print(array[k], end=" ")


    
