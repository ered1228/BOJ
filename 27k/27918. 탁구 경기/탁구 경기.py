import sys
input = sys.stdin.readline

n = int(input())
a = 0
b = 0
while True:
    winner = str(input())
    if winner == 'D\n':
        a += 1
    else:
        b += 1
    n -= 1
    if n == 0 or abs(a-b) == 2:
        print("{}:{}".format(a, b))
        break