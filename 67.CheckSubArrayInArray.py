array = list(map(int,input("Enter the array: ").split()))
subArray = list(map(int,input("Enter the subArray: ").split()))

# 1 2 3 4 5 6 7 8 4 5 6
# 4 5 6 7 8
count=0
i=0
while i< len(array):
    for j in range(len(subArray)):
        if array[i] == subArray[j]:
            count+=1
            i+=1
        elif count== len(subArray):
            print("Yes")
            break
        else:
            count=0
            i+=1
            break

else:
    print("No")

