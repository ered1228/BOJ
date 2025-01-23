from math import comb
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    print(comb(n, k))