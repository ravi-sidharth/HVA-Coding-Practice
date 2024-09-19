string = str(input("Enter the string: ").split())
char = str(input("Enter the char: "))

count =0
for i in range(len(string)):
    if string[i]== char:
        count+=1
    
if count == 0:
    print("No")

else:
    print(count)