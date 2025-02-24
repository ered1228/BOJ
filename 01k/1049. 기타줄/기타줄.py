n, m = map(int, input().split())
pack = float('inf')
one = float('inf')

for _ in range(m):
    a, b = map(int, input().split())
    pack = min(pack, a)
    one = min(one, b)

p, o = n//6, n%6
if o*one > pack:
    print((p+1)*pack)
elif 6*one < pack:
    print(n*one)
else:
    print((p*pack) + (o*one))