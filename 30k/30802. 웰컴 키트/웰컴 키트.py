n = int(input())
S = list(map(int, input().split()))
t, p = map(int, input().split())

T = [(s // t + 1) if (s % t) != 0 else s // t for s in S]
print(sum(T))
print(n//p, n%p)