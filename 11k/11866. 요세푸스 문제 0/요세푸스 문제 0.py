from collections import deque

m, k = map(int, input().split())
A = [i for i in range(1, m+1)]
A = deque(A)
res = []

while len(A) != 0:
    for _ in range(k-1):
        A.append(A.popleft())
    res.append(A.popleft())

r = ", ".join(map(str, res))
output = "<" + r + ">"
print(output)