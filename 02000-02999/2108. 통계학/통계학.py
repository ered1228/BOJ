# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

from collections import Counter
from statistics import median
import sys
input = sys.stdin.readline

def mpv(P):
    c = Counter(P)
    V = []
    order = c.most_common()
    maxv = order[0][1]
    for o in order:
        if o[1] == maxv:
            V.append(o[0])
    V.sort()
    if len(V) == 1:
        return V[0]
    else:
        return V[1]
    
P = []
n = int(input())
for _ in range(n):
    a = int(input())
    P.append(a)

avg = sum(P) / n
print(round(avg))
print(median(P))
print(mpv(P))
print(max(P) - min(P))