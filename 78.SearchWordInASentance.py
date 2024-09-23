S = str(input())
W = str(input())
count=0

for i in range(len(S)):

    if S[i] == W[count]:
        count+=1
        print(count)
        if count == len(W):
            print("Yes")
            quit()
    else:
        count =0

print("No")
