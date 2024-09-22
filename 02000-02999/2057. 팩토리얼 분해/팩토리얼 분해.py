def fac(t):
    r = 1
    for i in range(1, t+1):
        r *= i
    return r

n = int(input())
A = []

for i in range(21):
    if fac(i) > n:
        break
    A.append(fac(i))

if n == 0 or n > sum(A):
    print("NO")
else:
    print("YES")