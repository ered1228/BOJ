import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
task = int(input())

stack = [task]
vis = set()
cnt = -1
while stack:
    temp = stack.pop()
    if temp not in vis:
        vis.add(temp)
        cnt += 1
        for n in graph[temp]:
            stack.append(n)
print(cnt)