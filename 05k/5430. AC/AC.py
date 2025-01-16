from collections import deque
import sys
input = sys.stdin.readline

def f(operators, n, arr):
    rev = False
    for op in operators:
        if op == 'R':
            rev = not rev
        elif op == 'D':
            if not arr:
                return 'error'
            elif not rev:
                arr.popleft()
            else:
                arr.pop()
    return list(reversed(arr)) if rev else arr

t = int(input())
for _ in range(t):
    operators = str(input().strip())
    n = int(input())
    arr = str(input().strip())
    if arr == '[]':
        arr = deque()
    else:
        arr = deque(map(int, arr[1:-1].split(',')))
    
    res = f(operators, n, arr)
    if res == 'error':
        print(res)
    else:
        print('[' + (',').join(map(str, res)) + ']')