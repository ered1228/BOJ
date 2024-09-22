from bisect import bisect_right, bisect_left

F = [-1, 1, 2]
while F[-1] <= 10**100:
    F.append(F[-1] + F[-2])

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        lower = bisect_left(F, a)
        upper = bisect_right(F, b)
        print(upper - lower)