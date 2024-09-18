array = list(map(int,input("Enter the array: ").split()))
subArray = list(map(int,input("Enter the subArray: ").split()))

# 1 2 3 4 5 6 7 8 4 5 6
# 4 5 6 7 8

count=0
for i in range(len(array)):

    if count == len(subArray):
         break
    
    if array[i] == subArray[count]:
        count+=1
        
    else:
        count=0

if count== len(subArray):
        print("Yes")

else:
    print("No")

