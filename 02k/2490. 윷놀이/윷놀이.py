def abcde(x):
    if x == 0:
        return 'E'
    elif x == 1:
        return 'A'
    elif x == 2:
        return 'B'
    elif x == 3:
        return 'C'
    else:
        return 'D'

f = list(map(int, input().split()))
s = list(map(int, input().split()))
t = list(map(int, input().split()))

r1 = f.count(0)
r2 = s.count(0)
r3 = t.count(0)

print(abcde(r1))
print(abcde(r2))
print(abcde(r3))