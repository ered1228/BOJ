n = int(input())
n -= 1
n *= 180
angle = list(map(int, input().split()))
n -= 2*sum(angle)
print(n)