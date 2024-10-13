n = int(input())
s = str(input())
v = max(s.count('N'), s.count('S'), s.count('W'), s.count('E'))
print(n-v)