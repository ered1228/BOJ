n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
R = A.difference(B)
R = list(R)
R.sort()
if len(R) == 0:
    print(0)
else:
    print(len(R))
    for r in R:
        print(r, end=" ")