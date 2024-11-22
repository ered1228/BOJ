s = str(input())
A = []
for i in range(len(s)):
    A.append(s[i:])
A.sort()
for a in A:
    print(a)