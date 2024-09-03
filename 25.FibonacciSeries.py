n = int(input("Enter the no. of fibonacci series: "))
a=0
b=1
for i in range(n):
    sum =a+b
    print(a, end=" ")
    a=b;
    b=sum;
