S1 = str(input("Enter First String: ")).lower()
S2 = str(input("Enter second String: ")).lower()

count=0
j=0
i=0

while i<len(S1):
        print(j)
        if S1[i]==" ":
            i+=1
            continue 
        elif S1[i]==S2[j]:
            count+1
            i+=1
            j=0
            break
        else:
             j+=1 

if count==len(S1) or count==len(S2):
     print(count)
     print("Yes")

else:
     print(count)
     print("No")
                
                

