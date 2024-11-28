n = int(input())
L = list(map(int, input().split()))

if n == 1:
    print(L[0])
else:
    L.sort(reverse=True)
    m = L[0]
    L = L[1:]
    print(m*(n-1)+sum(L))