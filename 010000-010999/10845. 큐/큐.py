import sys
input = sys.stdin.readline

n = int(input())
Q = []
for i in range(n):
    c = input().split()
    if c[0] == 'push':
        Q.append(c[1])
    elif c[0] == 'pop':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q.pop(0))
    elif c[0] == 'size':
        print(len(Q))
    elif c[0] == 'empty':
        if len(Q) == 0:
            print('1')
        else:
            print('0')
    elif c[0] == 'front':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[0])
    elif c[0] == 'back':
        if len(Q) == 0:
            print('-1')
        else:
            print(Q[-1])