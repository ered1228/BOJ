title = [0, 666, 1666, 2666, 3666, 4666, 5666]

n = int(input())
if n < 7:
    print(title[n])
else:
    tmp = 6660
    while len(title) <= n:
        tmp = str(tmp)
        if '666' in tmp:
            title.append(int(tmp))
        tmp = int(tmp)
        tmp += 1
    print(title[-1])