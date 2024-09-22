a, b = map(int, input().split())
N = []
cnt = 0
res = 0

for i in range(1, 101):
    cnt += 1
    for j in range(cnt):
        N.append(i)
        
for k in range(a-1, b):
    res += N[k]

print(res)