#push X: 정수 X를 큐에 넣는 연산이다.
#pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 큐에 들어있는 정수의 개수를 출력한다.
#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque

queue = []
queue = deque(queue)
n = int(input())

for i in range(n):
    c = input().split()
    if c[0] == 'push':
        queue.append(c[1])
    elif c[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print('-1')
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif c[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])