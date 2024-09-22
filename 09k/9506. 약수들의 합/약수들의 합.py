import sys
input = sys.stdin.readline

def sf(x):
    F = [1]
    if x == 1:
        print('1 is NOT perfect.')
    else:
        for i in range(2, x):
            if x % i == 0:
                F.append(i)
        if sum(F) == x:
            print(x, "=", " + ".join(map(str, F)))
        else:
            print("{0} is NOT perfect.".format(x))

while True:
    n = int(input())
    if n == -1:
        break
    else:
        sf(n)