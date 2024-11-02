n = int(input())
Me = str(input())
Guile = str(input())
v = 0 ; d = 0

for i in range(n):
    if Me[i] == 'R':
        if Guile[i] == 'R':
            pass
        elif Guile[i] == 'S':
            v += 1
        else:
            d += 1
    elif Me[i] == 'S':
        if Guile[i] == 'S':
            pass
        elif Guile[i] == 'R':
            d += 1
        else:
            v += 1
    else:
        if Guile[i] == 'P':
            pass
        elif Guile[i] == 'R':
            v += 1
        else:
            d += 1

if v > d:
    print('victory')
else:
    print('defeat')