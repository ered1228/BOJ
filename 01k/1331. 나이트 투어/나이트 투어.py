C = [[0]*6 for _ in range(6)]

def is_not_knight(a, b, c, d):
    if a == c or b == d:
        return True
    elif abs(a - c) == 2 and abs(b - d) == 1:
        return False
    elif abs(a - c) == 1 and abs(b - d) == 2:
        return False
    else:
        return True

def same(H, low, column):
    if [low, column] in H:
        return True
    return False

H = []
cnt = 0
for i in range(36):
    move = str(input().strip())
    column = ord(move[0]) - ord('A')
    low = int(move[1]) - 1

    if same(H, low, column):
        print("Invalid")
        break
    else:
        H.append([low, column])
        cnt += 1
        if cnt >= 2:
            a = H[-1][0]
            b = H[-1][1]
            c = H[-2][0]
            d = H[-2][1]
            if is_not_knight(a, b, c, d):
                print("Invalid")
                break
else:
    a = H[0][0]
    b = H[0][1]
    c = H[-1][0]
    d = H[-1][1]
    if is_not_knight(a, b, c, d):
        print("Invalid")
    else:
        print("Valid")