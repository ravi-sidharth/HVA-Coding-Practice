D = int(input("Enter the Number: "))

binary=""

while D>0:
    if D%2==0:
        binary+=0
        print(binary)
    else:
        binary+=1
    D=D//2
print(binary)
