import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
for _ in range(n):
    a = int(input())
    A.append(a)

if n == 1:
    print(max(A) // k)
else:
    temp = 0
    start = 1 ; end = max(A) ; mid = (start + end) // 2
    while start <= end:
        mid = (start + end) // 2
        res = 0
        for a in A:
            res += a // mid
        if res >= k:
            start = mid + 1
        elif res < k:
            end = mid - 1
    print(end)