from collections import deque, defaultdict

n = int(input())
S = list(map(int, input().split()))
S_idx = defaultdict(int)
for i in range(n):
    S_idx[S[i]] = i

stack = deque([])
I = []

A = S[::-1]
for i in range(n):
    temp = A.pop()
    if not stack:
        stack.append(temp)
        I.append(0)
    else:
        while stack and stack[-1] < temp: #monotonic decreasing stack
            stack.pop()
        if not stack:
            I.append(0)
        else:
            I.append(S_idx[stack[-1]]+1)
        stack.append(temp)

print(' '.join(map(str, I)))