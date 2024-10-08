n = int(input())
res = n
while True:
    res += 1
    res = str(res)
    if res.count('0') == 0:
        print(res)
        break
    res = int(res)