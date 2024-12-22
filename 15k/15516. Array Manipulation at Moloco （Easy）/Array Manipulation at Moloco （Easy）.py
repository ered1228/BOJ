import sys
input = sys.stdin.readline

n = int(input())
A = [0]
S = [0]*(n+1)
for _ in range(n):
    A.append(int(input()))

for i in range(1, n+1):
    for j in range(1, i):
        if A[j] < A[i]:
            S[i] += 1

for s in S[1:]:
    print(s)