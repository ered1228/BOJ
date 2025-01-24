n = int(input())
fs = [] ; fe = []
for _ in range(n):
    s, e = map(int, input().split())
    fs.append(s)
    fe.append(e)
fs.sort(reverse=True)
fe.sort()
print(max(0, fs[0]-fe[0]))