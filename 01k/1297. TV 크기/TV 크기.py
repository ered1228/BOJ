import math

D, h, w = map(int, input().split())
k = math.sqrt((D**2)/(h**2 + w**2))
print(math.floor(h*k), math.floor(w*k))