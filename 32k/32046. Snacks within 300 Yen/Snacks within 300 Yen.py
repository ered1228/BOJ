import sys
input = sys.stdin.readline

def snack(n, S):
    a = 0
    for s in S:
        if a + s <= 300:
            a += s
        else:
            pass
    return a

while True:
    n = int(input())
    if n == 0:
        break
    else:
        S = list(map(int, input().split()))
        print(snack(n, S))