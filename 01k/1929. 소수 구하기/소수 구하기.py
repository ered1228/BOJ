import math

def j_prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
        return True

m, n = map(int, input().split())
for j in range(m, n+1):
    if j_prime(j):
        print(j)