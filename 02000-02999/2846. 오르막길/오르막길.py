n = int(input())
path = list(map(int, input().split()))
M = []
T = []

for i in range(n-1):
    if path[i] < path[i+1]:
        M.append(path[i])
        M.append(path[i+1])
    else:
        if len(M) != 0:
            tmp = M[-1] - M[0]
            T.append(tmp)
        M.clear()

if len(M) != 0: #마지막 루프 처리
    tmp = M[-1] - M[0]
    T.append(tmp)

if len(T) == 0:
    print(0)
else:
    print(max(T))