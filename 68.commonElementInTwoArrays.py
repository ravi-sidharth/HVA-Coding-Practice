n =int(input("Enter the same common length: "))  #7
arr1 = list(map(int,input("Enter the first array: ").split()))   # 4 9 2 5 7 4 3
arr2 = list(map(int,input("Enter the second array: ").split()))   # 9 6 4 8 6 1 12

for i in range(n):
    for j in range(n):
        if arr1[i]==arr2[j]:
            print(arr2[j],end=" ")
            arr2[j]=0
            break
print()

