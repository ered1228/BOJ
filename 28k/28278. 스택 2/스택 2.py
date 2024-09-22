import sys
input = sys.stdin.readline

stack = []
n = int(input())

for i in range(n):
    c = input().split()
    if c[0] == '1':
        stack.append(c[1])
    elif c[0] == '2':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print('-1')
    elif c[0] == '3':
        print(len(stack))
    elif c[0] == '4':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif c[0] == '5':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])