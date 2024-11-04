a, b, c = map(int, input().split())
T = [a, b, c]
T.sort()

if T[2] < T[1] + T[0]:
    print(sum(T))
else:
    while T[2] >= T[1] + T[0]:
        T[2] -= 1
    print(sum(T))