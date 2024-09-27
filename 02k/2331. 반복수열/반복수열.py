A, p = map(int, input().split())
A = str(A)
D = [A]

while True:
    temp = 0
    for a in D[-1]:
        a = int(a)
        temp += a**p
    temp = str(temp)
    if temp in D:
        inx = D.index(temp)
        D = D[:inx]
        break
    else:
        D.append(temp)
print(len(D))