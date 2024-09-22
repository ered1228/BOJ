n = int(input())
for i in range(n):
    s = str(input())
    l = len(s)
    if l >= 6 and l <= 9:
        print("yes")
    else:
        print("no")