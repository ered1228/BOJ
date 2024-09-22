from collections import deque

n = int(input())
Q = deque(range(1, n+1))

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())
    
print(Q[0])