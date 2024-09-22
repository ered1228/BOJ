import sys
input = sys.stdin.readline

P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    P.append(P[i-1] + P[i-5])

t = int(input())
for _ in range(t):
    n = int(input())
    print(P[n])