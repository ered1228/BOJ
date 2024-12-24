n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    c5 = n // 5
    n %= 5
    while n % 2 != 0:
        n += 5
        c5 -= 1
    c2 = n // 2
    print(c5 + c2)