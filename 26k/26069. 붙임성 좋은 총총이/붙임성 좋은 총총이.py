dance = []
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if a == 'ChongChong':
        dance.append(a)
        dance.append(b)
    elif b == 'ChongChong':
        dance.append(a)
        dance.append(b)
    elif a in dance:
        dance.append(b)
    elif b in dance:
        dance.append(a)
    else:
        pass
print(len(list(set(dance))))