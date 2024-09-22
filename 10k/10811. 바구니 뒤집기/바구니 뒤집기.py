n, m = map(int, input().split())
A = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = A[i-1:j][::-1]
    A[i-1:j] = temp

for a in A:
    print(a, end = ' ')