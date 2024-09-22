st = input().upper()
li = [-1]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(alpha)):
    temp = st.count(alpha[i])
    li.append(temp)

inx = li.index(max(li))

if li.count(max(li)) == 1:
    print(alpha[inx-1])
else:
    print("?")