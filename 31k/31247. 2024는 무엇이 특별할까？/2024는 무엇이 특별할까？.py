import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k > 60:
        print(0)
    else:
        exp = 2**k
        temp = n // exp
        if temp % 2 == 0:
            res = temp // 2
        else:
            res = (temp // 2) + 1
        print(res)