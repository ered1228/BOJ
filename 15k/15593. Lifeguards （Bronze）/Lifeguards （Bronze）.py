import sys
input = sys.stdin.readline

n = int(input())
T = [0]*1001
L = []
R = []

for _ in range(n):
    a, b = map(int, input().split())
    L.append([a, b])

for i in range(n):
    tmp = L[i]
    L.remove(tmp)
    for j in range(n-1):
        for k in range(L[j][0], L[j][1]):
            T[k] = 1
    R.append(T.count(1))
    T = [0]*1001
    L.insert(i, tmp)

print(max(R))