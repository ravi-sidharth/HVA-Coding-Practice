array = list(map(int,input().split()))

repeat=False
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] == array[j]:
            print(array[i])
            repeat=True
            break
    if repeat== True:
        break 