t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        name, toy = input().split()
        if name in dic:
            dic[name] += int(toy)
        else:
            dic[name] = int(toy)
    A = sorted(dic.items(), key=lambda x : (-x[1], x[0]))
    print(len(A))
    for a in A:
        print(a[0], a[1])