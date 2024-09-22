import sys
input = sys.stdin.readline

def extended_Euclidean(r1, r2, s1, s2, t1, t2):
    while r2 != 0:
        q = r1 // r2
        r = r1 - (q * r2)
        s = s1 - (q * s2)
        t = t1 - (q * t2)
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t
    return [r1, s1, t1]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 1 and b == 1:
        print(2)
    elif a == 1 and b != 1:
        print(1)
    elif a != 1 and b == 1:
        if a+1 <= 1000000000:
            print(a+1)
        else:
            print("IMPOSSIBLE")
    else:
        A = extended_Euclidean(-a, b, 1, 0, 0, 1)
        if A[0] != 1:
            print("IMPOSSIBLE")
        else:
            while A[2] <= 0:
                A[2] += a
            if A[2] > 1000000000:
                print("IMPOSSIBLE")
            else:
                print(A[2])