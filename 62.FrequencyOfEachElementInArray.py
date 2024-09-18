array = list(map(int,input("Enter the array: ").split()))

for i in range(len(array)):
    count =1 
    for j in range(i+1,len(array)):

        if array[i] is None:
            break

        if array[i]==array[j]:
            array[j]=None
            count+=1

    if array[i] is not None:
        print(array[i],count, end=" ")
        print()


