import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

nums = [i for i in range(n, 0, -1)]
stack = [] ; res = []
isprint = True

start = A[0]
A = A[1:]

for _ in range(1, start+1):
    stack.append(nums.pop())
    res.append('+')
stack.pop()
res.append('-')

for a in A:
    if len(stack) > 0 and a >= stack[-1]:
        while a > stack[-1]:
            if len(nums) > 0:
                stack.append(nums.pop())
                res.append('+')
            else:
                isprint = False
                break
        stack.pop()
        res.append('-')
    elif len(stack) > 0 and a < stack[-1]:
        isprint = False
        break
    else: #len(stack) == 0
        while True:
            stack.append(nums.pop())
            res.append('+')
            if stack[-1] == a:
                break
        stack.pop()
        res.append('-')
        
if isprint:
    for r in res:
        print(r)
else:
    print('NO')