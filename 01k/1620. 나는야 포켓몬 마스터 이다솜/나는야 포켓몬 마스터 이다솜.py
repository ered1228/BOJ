import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Idic = [0]*(n+2)
Ndic = {}
for i in range(n):
    name = str(input().strip())
    Idic[i+1] = name
    Ndic[name] = i+1
for j in range(m):
    find = input().strip()
    if find.isdigit():
        print(Idic[int(find)])
    else:
        print(Ndic[find])