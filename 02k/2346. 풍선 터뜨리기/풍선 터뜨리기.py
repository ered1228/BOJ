from collections import deque

n = int(input())
A = deque([i for i in range(1, n+1)])
S = list(map(int, input().split()))
R = [A[0]]
if len(A) == 1:
    print(R[0])
else:
    while True:
        step = S[A[0]-1]
        if step > 0:
            A.popleft()
            A.rotate(-(step-1))
            R.append(A[0])
            if len(A) == 1:
                break
        else:
            A.popleft()
            A.rotate(-step)
            R.append(A[0])
            if len(A) == 1:
                break

for r in R:
    print(r, end=' ')