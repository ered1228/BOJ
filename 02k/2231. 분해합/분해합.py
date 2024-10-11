generator = []
n = int(input())
for i in range(1, n+1):
    res = i
    temp = str(i)
    for j in range(len(temp)):
        res += int(temp[j])
    if res == n:
        generator.append(i)
if len(generator) == 0:
    print(0)
else:
    print(min(generator))