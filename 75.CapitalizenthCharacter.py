String = str(input("Enter the String: "))
index= int(input("Enter the index no.: "))

newString=""
for i in range(len(String)):
    if i== index:
        newString+= String[i].upper()
    else:
        newString+=String[i]
print(newString)