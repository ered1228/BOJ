a, b = map(int, input().split())
i = a % 4
j = b % 4

if i != 0 and j != 0:
    c = abs((a//4) - (b//4))
    d = abs((a%4) - (b%4))
    print(c+d)
elif (i == 0 and j != 0):
    a -= 1
    c = abs((a//4) - (b//4))
    d = abs((a%4) - (b%4))
    print(c+d+1)
elif (i != 0 and j == 0):
    b -= 1
    c = abs((a//4) - (b//4))
    d = abs((a%4) - (b%4))
    print(c+d+1)
else:
    print(abs((a//4)-(b//4)))