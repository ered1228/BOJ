n = int(input())
level = list(map(int, input().split()))

for l in level:
    if l == 300:
        print('1', end=' ')
    elif l < 300 and l >= 275:
        print('2', end = ' ')
    elif l < 275 and l >= 250:
        print('3', end=' ')
    else:
        print('4', end=' ')