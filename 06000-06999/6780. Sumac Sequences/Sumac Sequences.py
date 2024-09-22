t1 = int(input())
t2 = int(input())

S = [t1, t2]
while True:
    S.append(t1 - t2)
    t1 = t2
    t2 = S[-1]
    if t1 < t2:
        break
print(len(S))