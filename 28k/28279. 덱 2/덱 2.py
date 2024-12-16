from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
D = deque([])
for _ in range(n):
    c = input().rstrip().split()
    if c[0] == '1':
        D.appendleft(c[1])
    elif c[0] == '2':
        D.append(c[1])
    elif c[0] == '3':
        if D:
            print(D.popleft())
        else:
            print(-1)
    elif c[0] == '4':
        if D:
            print(D.pop())
        else:
            print(-1)
    elif c[0] == '5':
        print(len(D))
    elif c[0] == '6':
        if D:
            print(0)
        else:
            print(1)
    elif c[0] == '7':
        if D:
            print(D[0])
        else:
            print(-1)
    elif c[0] == '8':
        if D:
            print(D[-1])
        else:
            print(-1)