C = [[0 for _ in range(101)] for _ in range(101)]

for ii in range(4):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            C[y][x] += 1

res = 0
for c in C:
    res += c.count(1)
    res += c.count(2)
    res += c.count(3)
    res += c.count(4)
print(res)