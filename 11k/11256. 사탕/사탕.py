t = int(input())
for _ in range(t):
    candy, n = map(int, input().split())
    box = []
    res = 0 ; cnt = 0
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r*c)
    
    box.sort(reverse=True)
    for b in box:
        res += b
        cnt += 1
        if res >= candy:
            break
    print(cnt)