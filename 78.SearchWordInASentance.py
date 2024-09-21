S = str(input())
W = str(input())
count=0

for i in range(len(S)):

    if S[i] == W[count]:
        count+=1
        print(count)
        print(len(W))
    elif count == len(W):
        print("Yes")
        break

    else:
        count =0

else:
    print("No")
