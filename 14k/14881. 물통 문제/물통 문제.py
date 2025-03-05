import sys
input = sys.stdin.readline

def Euclidean(a, b, r):
    if b == 0:
        return r
    elif a < b:
        return Euclidean(b, a%b, r)
    else:
        r.append(a%b)
        return Euclidean(b, a%b, r)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    answer = "NO"
    if c > max(a, b):
        print("NO")
    elif a % c == 0 or b % c == 0:
        print("YES")
    else:
        for r in Euclidean(a, b, []):
            if r != 0 and c % r == 0:
                answer = "YES"
                break
        print(answer)