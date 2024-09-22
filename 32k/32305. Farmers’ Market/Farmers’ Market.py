a, b = map(int, input().split())
c = int(input())
d = a*b
if d % 12 == 0:
    print(c*(d//12))
else:
    print(c*((d//12) + 1))