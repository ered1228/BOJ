n = int(input())
current = 1
length = 1
if n % 2 == 0 or n % 5 == 0:
    print(-1)
else:
    while current % n != 0:
        current = (current*10 + 1) % n
        length += 1
    print(length)
