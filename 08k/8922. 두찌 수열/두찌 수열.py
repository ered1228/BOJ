import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    T = list(map(int, input().split()))
    tup = [0]*n
    vis = set(tuple(T))
    while True:
        new_T = []
        for i in range(n-1):
            new_T.append(abs(T[i]-T[i+1]))
        new_T.append(abs(T[0]-T[-1]))
        if tuple(new_T) in vis:
            print('LOOP')
            break
        elif new_T == tup:
            print('ZERO')
            break
        else:
            vis.add(tuple(new_T))
            T = new_T