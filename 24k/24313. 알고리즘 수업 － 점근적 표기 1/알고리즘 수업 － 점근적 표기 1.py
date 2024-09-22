a, b = map(int, input().split())
c = int(input())
n = int(input())

if c > a:
    if n >= (b/(c-a)):
        print(1)
    else:
        print(0)
elif a == c:
    if b > 0:
        print(0)
    else:
        print(1)
else:
    print(0)