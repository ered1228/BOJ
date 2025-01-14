from collections import deque

n = int(input())
A = deque(list(map(int, input().split())))
S = deque([])

out = 1
while True:
    if len(S) > 0 and S[-1] == out:
        S.pop()
        out += 1
    elif len(A) == 0:
        break
    else:
        S.append(A.popleft())
        if S[-1] == out:
            S.pop()
            out += 1

if len(S) == 0:
    print('Nice')
else:
    print('Sad')