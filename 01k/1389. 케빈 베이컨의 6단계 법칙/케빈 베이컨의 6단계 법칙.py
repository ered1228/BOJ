from collections import deque

def BFS(graph, start, target):
    visit = set()
    queue = deque([(start, 0)])
    
    while queue:
        temp, cnt = queue.popleft()
        if target == temp:
            return cnt
        else:
            if temp not in visit:
                visit.add(temp)
                S = list(set(graph[temp]) - set(visit))
                for s in S:
                    queue.append((s, cnt+1))

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
people = [[0]*n for _ in range(n)]
res = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n+1):
    for k in range(1, n+1):
        if j != k:
            people[j-1][k-1] = BFS(graph, j, k)

res = [(l+1, sum(people[l])) for l in range(n)]
res.sort(key=lambda x : (x[1], x[0]))
print(res[0][0])