#꼭짓점 - 모서리 + 면 = 2

t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    print(2 - v + e)