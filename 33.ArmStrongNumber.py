n = int(input())
a=n
b=n
count=0
sum=0

while a>0:
    count+=1
    a = a//10

while b>0:
    remain = b%10
    sum+=remain**count
    b=b//10

if n == sum:
    print("Yes")
else:
    print("No")
