st = str(input())
A = []
for _ in range(97, 123):
    for i in range(len(st)):
        result = -1
        if chr(_) == st[i]:
            result = i
            break
    print(result, end=" ")