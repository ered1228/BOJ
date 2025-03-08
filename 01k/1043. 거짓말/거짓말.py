import sys
input = sys.stdin.readline

def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]

def union(a, b):
    a = find(a) ; b = find(b)
    if a > b:
        root[b] = a
    else:
        root[a] = b

n, m = map(int, input().split())
truth = list(map(int, input().split()))
root = [i for i in range(n+1)]
party_list = []
for _ in range(m):
    party = list(map(int, input().split()))
    party_list.append(party[1:])
    l = party[0]
    for i in range(1, l):
        union(party[i], party[i+1])

cnt = 0
truth = set([find(t) for t in truth[1:]])
for pi in party_list:
    s = True
    for p in pi:
        if find(p) in truth:
            s = False
            break
    if s:
        cnt += 1

print(cnt)