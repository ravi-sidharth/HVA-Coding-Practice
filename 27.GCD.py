a = int(input("Enter first positive number: "))
b = int(input("Enter second positive number: "))

lowestNumber =0
hcf=0

if a<b:
    lowestNumber=a;
else:
    lowestNumber=b;

for i in range(1,lowestNumber+1):
    if a%i==0 and b%i==0:
        hcf=i

print(hcf)