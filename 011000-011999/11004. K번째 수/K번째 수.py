import sys
n, k = map(int, sys.stdin.readline().split())
I = list(map(int, sys.stdin.readline().split()))
I.sort()
print(I[k-1])