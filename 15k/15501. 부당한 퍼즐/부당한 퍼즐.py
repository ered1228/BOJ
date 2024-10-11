n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
d1 = [] ; d2 = []

st1 = s1.index(1)
for i in range(st1, st1+n):
    temp = s1[i % n] - s1[(i+1) % n]
    d1.append(temp)
        
st2 = s2.index(1)
for j in range(st2, st2+n):
    temp = s2[j % n] - s2[(j+1) % n]
    d2.append(temp)

if d1 == d2:
    print("good puzzle")
else:
    d2.reverse()
    for k in range(n):
        d2[k] *= -1
    if d1 == d2:
        print("good puzzle")
    else:
        print("bad puzzle")