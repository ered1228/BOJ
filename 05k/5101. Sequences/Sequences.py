def find_inx(a, b, c):
    i = 1
    if a == c:
        return 1
    else:
        while True:
            i += 1
            a += b
            if a == c:
                return i

while True:
    start, diff, find = map(int, input().split())
    if start == 0 and diff == 0 and find == 0:
        break
    else:
        if abs(start - find) % abs(diff) != 0:
            print('X')
        elif diff > 0 and start > find:
            print('X')
        elif diff < 0 and start < find:
            print('X')
        else:
            print(find_inx(start, diff, find))