n = int(input("Enter the number of n terms: "))

k=1
count=0
i=1
while i<=n:
    j=1
    while True:
        if (j>k):
            break
        if (k%j==0):
            count+=1
            j+=1
        else:
            j+=1

    if count ==2:
        print(k,end=" ")
        k+=1
        i+=1
        count=0
    else: 
        k+=1
        count=0
        
     
        
