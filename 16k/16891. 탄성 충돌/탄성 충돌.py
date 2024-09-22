import math

n = int(input())
p = math.pi
if n == 1:
    print(3)
else:
    n = n**2
    f = int(p / math.atan(math.sqrt(1/n)))
    print(f)