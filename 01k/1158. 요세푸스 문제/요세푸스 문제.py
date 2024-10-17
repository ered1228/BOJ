from collections import deque

n, k = map(int, input().split())
A = [i for i in range(1, n+1)]
A = deque(A)
res = []

while True:
    for _ in range(k-1):
        A.append(A.popleft())
    res.append(A.popleft())
    if len(res) == n:
        break

output = ", ".join(str(s) for s in res)
output = '<' + output
output = output.rstrip()
output = output + ">"
print(output)
# <3, 6, 2, 7, 5, 1, 4>