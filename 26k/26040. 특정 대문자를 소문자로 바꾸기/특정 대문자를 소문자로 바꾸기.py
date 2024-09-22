s = str(input())
B = list(input().split())

for b in B:
    s = s.replace(b, b.lower())

print(s)