n = int(input())
A, B = 0, 0
res = True
for _ in range(n):
    a, b = map(int, input().split())
    if a >= A and b >= B:
        A = a ; B = b
    else:
        res = False
if res:
    print("yes")
else:
    print("no")