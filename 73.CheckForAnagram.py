S1 = str(input("Enter First String: ")).lower().replace(" ", "")
S2 = str(input("Enter second String: ")).lower().replace(" ","")

count=0
j=0
i=0
print(len(S1))
print(len(S2))
while i<len(S1):
    # if j ==len(S2):
    #     print("No")
    #     quit()

    if S1[i]==S2[j]:
        count+=1
        i+=1
        j=0
    else:
        j+=1 

if count==len(S1) or count==len(S2):
     print("Yes")

else:
     print("No")
                
                

