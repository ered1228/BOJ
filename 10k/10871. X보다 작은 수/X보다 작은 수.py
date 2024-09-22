n, x = map(int, input().split())
A = list(map(int, input().split()))
B = []
for a in A:
    if a < x:
        B.append(a)
for b in B:
    print(b, end=' ')