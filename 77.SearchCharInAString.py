S = str(input("Enter the String: "))
C = str(input("Enter the target Char: "))

for char in range(len(S)):
    if S[char]== C:
        print ("Yes")
        quit()

print("No")