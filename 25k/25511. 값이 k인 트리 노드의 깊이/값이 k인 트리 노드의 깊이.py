import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = {i:[] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
node = list(map(int, input().split()))
r = node.index(k)

stack = [(0, 0)]
while stack:
    temp, d = stack.pop()
    if temp == r:
        print(d)
        break
    for nex in graph[temp]:
        stack.append((nex, d+1))