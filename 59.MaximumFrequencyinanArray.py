# 5 4 7 11 8 4 6 11 9

n=list(map(int,input().split()))
count=0
maxCount=0
max =0
for i in range(len(n)):
    j=i+1
    for j in range (len(n)):
        if n[i]==n[j]:
            count+=1
    if count>maxCount:
        maxCount=count
        max=n[i]

    count=0
print(max)
