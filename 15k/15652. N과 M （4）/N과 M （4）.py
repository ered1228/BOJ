def DFS(a):
    vis = []
    stack = [a]
    while stack:
        temp = stack.pop()
        if len(temp) == m:
            vis.append(temp)
        else:
            for i in range(n, temp[-1]-1, -1):
                stack.append(temp + [i])
    return vis

n, m = map(int, input().split())
A = [[1], [2], [3], [4], [5], [6], [7], [8]]
A = A[:n]
res = []
for a in A:
    res.append(DFS(a))

for i in range(len(res)):
    for j in range(len(res[i])):
        print(' '.join(map(str, res[i][j])))