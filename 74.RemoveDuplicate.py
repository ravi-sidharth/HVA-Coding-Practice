String = str(input("Enter the String: ")).lower().replace(" ","")

# programming
for i in range(len(String)):
    flag = True
    for j in range(i):
        if String[i]== String[j]:
            flag = False
    if flag:
        print(String[i], end='')
