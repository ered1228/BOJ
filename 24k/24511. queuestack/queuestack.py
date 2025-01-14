from collections import deque

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

Q = deque([])
for i in range(n):
    if A[i] == 0:
        Q.append(B[i])

for j in range(m):
    Q.appendleft(C[j])
    print(Q.pop(), end=' ')