#  4 6 7 2 8 9 3 10 
# 10

array = list(map(int,input("Enter the array: ").split())) 
targetSum = int(input("Enter the target sum: "))

count=0
for i in range( len(array)):
    for j in range(i+1,len(array)):
        if (array[i]+array[j]==targetSum):
            print(array[i], array[j], end =" ")
            print()
            break

