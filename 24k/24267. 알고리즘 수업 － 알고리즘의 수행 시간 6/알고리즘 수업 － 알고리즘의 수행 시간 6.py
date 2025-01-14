n = int(input())
if n == 0 or n == 1:
    print(0)
    print(3)
else:
    res = 0
    for i in range(1, n-1):
        res += i*(n-1-i)
    print(res)
    print(3)