def cantor(n, C):
    l = 3**n
    if n == 0:
        return C
    else:
        C1 = C[0:(l//3)] ; C3 = C[(l//3)*2:]
        return cantor(n-1, C1) + ' '*(l//3) + cantor(n-1, C3)

while True:
    try:
        n = int(input())
        C = '-'*(3**n)
        print(cantor(n, C))
    except:
        break