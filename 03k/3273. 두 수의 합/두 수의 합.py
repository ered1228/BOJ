n = int(input())
P = list(map(int, input().split()))
x = int(input())

cnt = 0
P = set(P)
for p in P:
    if (x-p) in P:
        if x-p != p:
            cnt += 1
print(cnt//2)