import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    print(min(A), max(A))