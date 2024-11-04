import sys
input = sys.stdin.readline

n = int(input())
p = set()

for _ in range(n):
    a, b = map(str, input().split())
    if b == 'enter':
        if a not in p:
            p.add(a)
    else:
        if a in p:
            p.discard(a)
p = list(p)
p.sort(reverse=True)
for ele in p:
    print(ele)