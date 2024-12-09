import math

n = int(input())
m = 2*n
m = math.sqrt(m)

for i in range(int(m)+2, 0, -1):
    if i*(i+1) <= n*2:
        print(i)
        break