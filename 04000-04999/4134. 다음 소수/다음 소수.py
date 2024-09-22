import sys
import math
input = sys.stdin.readline

def prime(x):
    if x <= 1:
        return -1
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return -1
        return x

def next_prime(n):
    while True:
        tmp = prime(n)
        if tmp == n:
            return n
        else:
            n += 1
            return next_prime(n) 

t = int(input())
for _ in range(t):
    n = int(input())
    print(next_prime(n))