t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    n = 0
    while True:    
        if n*(n+1) >= d:
            if (n**2) < d:
                result = 2*n
            else:
                result = (2*n)-1
            break
        n += 1
    print(result)