from bisect import bisect_left
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        S = [0]+list(map(int, input().split()))
        mv = [0]
        for i in range(1, n+1):
            temp = S[i]
            idx = bisect_left(mv, temp)
            if idx == len(mv):
                mv.append(temp)
            else:
                mv[idx] = temp
        print(len(mv)-1)
    except:
        break