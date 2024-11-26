S = str(input())
l = len(S)
d = set()

for i in range(1, l+1):
    for j in range(l):
        s = S[j:j+i]
        if s not in d:
            d.add(s)
print(len(d))