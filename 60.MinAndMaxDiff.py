# 5 4 7 8 4 6 11 9
array = list(map(int,input().split()))
min=2**63-1
max=0

for i in range(len(array)-1):
    for j in range(i+1,len(array)-1):
        num=abs(array[i]-array[j])

        if num >max:
            max=num
            
        elif num<min:
            min=num
    
print(min,max)

