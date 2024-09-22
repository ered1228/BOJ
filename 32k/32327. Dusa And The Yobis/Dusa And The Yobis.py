import sys
input = sys.stdin.readline

d = int(input())
while True:
    y = int(input())
    if d > y:
        d += y
    else:
        print(d)
        break