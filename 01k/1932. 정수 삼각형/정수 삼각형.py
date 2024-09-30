import sys
input = sys.stdin.readline

n = int(input())
ini = int(input())
S = [[ini]]
for i in range(1, n):
    tri = list(map(int, input().split()))
    T = []
    TT = []
    for j in range(i):
        for k in range(j, j+2):
            T.append(S[i-1][j] + tri[k])
    TT.append(T[0])
    for l in range(1, len(T)-2, 2):
        TT.append(max(T[l], T[l+1]))
    TT.append(T[-1])
    S.append(TT)
print(max(S[-1]))