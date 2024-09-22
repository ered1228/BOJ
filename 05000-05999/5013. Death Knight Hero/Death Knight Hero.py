n = int(input())
cnt = 0
for _ in range(n):
    s = str(input())
    s = s.replace('CD', 'X')
    if s.count('X') < 1:
        cnt += 1
print(cnt)