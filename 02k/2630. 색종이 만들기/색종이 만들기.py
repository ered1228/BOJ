import sys
input = sys.stdin.readline

def all_blue_or_white(A):
    k = len(A)
    color = A[0][0]
    if color == 1:
        all_blue = True
        all_white = False
        for i in range(k):
            for j in range(k):
                if A[i][j] != color:
                    all_blue = False
                    break
    else:
        all_blue = False
        all_white = True
        for i in range(k):
            for j in range(k):
                if A[i][j] != color:
                    all_white = False
                    break
    if all_blue:
        return 'blue'
    elif all_white:
        return 'white'
    else:
        return 'try again'

n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().rstrip().split())))

ini = all_blue_or_white(A)
if ini == 'blue':
    print(0)
    print(1)
elif ini == 'white':
    print(1)
    print(0)
else:
    stack = [A] ; blue = 0 ; white = 0
    while stack:
        Arr = stack.pop()
        mid = len(Arr) // 2
        A1 = [row[:mid] for row in Arr[:mid]]
        A2 = [row[mid:] for row in Arr[:mid]]
        A3 = [row[:mid] for row in Arr[mid:]]
        A4 = [row[mid:] for row in Arr[mid:]] 
        B = [A1, A2, A3, A4]
        for b in B:
            res = all_blue_or_white(b)
            if res == 'blue':
                blue += 1
            elif res == 'white':
                white += 1
            else:
                stack.append(b)
    print(white)
    print(blue)