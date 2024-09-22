import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
S = [0]*(n+1)

for i in range(1, n+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(S[j] - S[i-1])