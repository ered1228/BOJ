n, k = map(int, input().split())
s = 1
m = 1
if (k == 0) or (k == n) :
    v = 1
else :
    for i in range(k+1, n+1):
        s *= i #분자
    for j in range(1, n-k+1):
        m *= j #분모
    v = s//m
print(v)