def f(a, b):
    dic = {0:[0], 1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}
    cycle = dic[a%10]
    length = len(cycle)
    if b >= length:
        inx = b % length - 1
        res = cycle[inx]
    else:
        inx = b - 1
        res = cycle[inx]
    if res != 0:
        return res
    else:
        return 10

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(f(a, b))