def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    gcd = Euclidean(a, b)
    print(gcd*(a//gcd)*(b//gcd))