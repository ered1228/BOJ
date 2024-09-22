from bisect import bisect_right
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n1 = int(input())
    N1 = list(map(int, input().split()))
    n2 = int(input())
    N2 = list(map(int, input().split()))
    N1.sort()
    for a in N2:
        if a <= N1[0]:
            if N1[0] == a:
                print(1)
            else:
                print(0)
        elif a >= N1[-1]:
            if N1[-1] == a:
                print(1)
            else:
                print(0)
        else:
            inx = bisect_right(N1, a)
            if N1[inx-1] == a:
                print(1)
            else:
                print(0)