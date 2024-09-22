a, b = map(int, input().split())
if a == b:
    print(1)
else:
    if a % 2 != 0 and b % 2 != 0:
        print((b-a)//2 + 1)
    elif a % 2 != 0 and b % 2 == 0:
        print(int((b-a)/2)+1)
    elif a % 2 == 0 and b % 2 == 0:
        print((b-a)//2 + 1)
    else:
        print(int((b-a)/2)+2)