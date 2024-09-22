t = int(input())
for i in range(t):
    a = str(input())
    l = len(a)
    test1 = a[(l//2) - 1]
    test2 = a[(l//2)]
    if test1 == test2:
        print("Do-it")
    else:
        print("Do-it-Not")