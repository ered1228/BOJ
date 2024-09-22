import math

def prime(x):
    if x == 1:
        return 0
    else:
        for j in range(2, int(math.sqrt(x) + 1)):
            if x % j == 0:
                return 0
        return x

m = int(input())
n = int(input())
A = []

for i in range(m, n+1):
    res = prime(i)
    if res != 0:
        A.append(res)

if len(A) == 0:
    print('-1')
else:
    print(sum(A))
    print(A[0])