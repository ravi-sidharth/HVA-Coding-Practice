b = int(input("Enter the binary number:")) 

decimal=0
i=0
while b>0:
    remain=b%10
    decimal+=remain*(2**i)
    b=b//10
    i+=1
print(decimal)