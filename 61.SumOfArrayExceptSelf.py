array = list(map(int,input().split()))
sum=0
count=0
i=0
while i<len(array):
    if count == i:
        count+=1
        continue
    if count == len(array):
        print(sum,end=" ")
        count=0
        sum=0
        i+=1
        continue

    sum+=array[count]
    count+=1