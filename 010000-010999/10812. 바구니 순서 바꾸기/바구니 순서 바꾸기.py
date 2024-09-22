n, m = map(int, input().split())
A = [a for a in range(1, n+1)]

for i in range(m):
    start, end, mid = map(int, input().split())
    start -= 1
    mid -= 1
    end -= 1
    A = A[:start] + A[mid:end+1] + A[start:mid] + A[end+1:]

for b in A:
    print(b, end=' ')