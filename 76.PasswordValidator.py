s = input()

con1, con2, con3, con4, con5 = False, False, False, False, False

if len(s)>=8:
    con1=True

for char in s:
    if char.isupper():
        con2 =True 
    elif char.islower():
        con3 = True
    elif char.isnumeric():
        con4 = True
    elif not char.isspace():
        con5 = True
    
con = all([con1,con2,con3,con4,con5])
print("Yes" if con else "No")
   