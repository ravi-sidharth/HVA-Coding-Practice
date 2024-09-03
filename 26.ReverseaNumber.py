n = int(input("Enter the number:"))

reverse =0
while n>0 :
    remain=n%10
    reverse=reverse*10+remain
    n=n//10

print(reverse)


