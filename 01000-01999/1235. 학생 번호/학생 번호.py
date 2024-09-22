n = int(input())
S = []
for _ in range(n):
    nu = str(input())
    S.append(nu)

l = len(S[0])
for i in range(1, l+1):
    RS = [s[l-i:] for s in S]
    a = len(RS)
    RS = set(RS)
    b = len(RS)
    if a == b:
        print(i)
        break
    else:
        pass