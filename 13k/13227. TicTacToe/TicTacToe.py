T = []

def row_check(T):
    R = []
    for i in range(3):
        if T[i] == "OOO":
            R.append(1)
        elif T[i] == "XXX":
            R.append(1)
        else:
            pass
    if 1 in R:
        return 1
    else:
        return 0

def diagonal_check(T):
    d1 = T[0][0] + T[1][1] + T[2][2]
    d2 = T[0][2] + T[1][1] + T[2][0]
    R = []
    if d1 == "OOO" or d2 == "OOO":
        R.append(1)
    elif d1 == "XXX" or d2 == "XXX":
        R.append(1)
    if 1 in R:
        return 1
    else:
        return 0

def column_check(T):
    C = []
    for i in range(3):
        C.append(T[0][i] + T[1][i] + T[2][i])
    return row_check(C)

for _ in range(3):
    T.append(str(input()))

row = row_check(T)
dia = diagonal_check(T)
col = column_check(T)
if row + dia + col > 0:
    print("YES")
else:
    print("NO")