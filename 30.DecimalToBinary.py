D = int(input("Enter the Number: "))

binary=""

while D>0:
    if D%2==0:
        binary+="0"
    else:
        binary+="1"
    D=D//2

revbinary=""
for i in range(len(binary)-1,-1,-1):
    revbinary+=binary[i]
print(revbinary)


