import sys
input = sys.stdin.readline

n = int(input())
w = []
h = []

for _ in range(n):
    info = list(map(int, input().split()))
    w.append(info[0])
    h.append(info[1])
    
for i in range(n):
    rank = 1
    for j in range(n):
        if w[i] < w[j] and h[i] < h[j]:
            rank += 1
    print(rank, end=" ")