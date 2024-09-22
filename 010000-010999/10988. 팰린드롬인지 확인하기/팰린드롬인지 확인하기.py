s = str(input())
if s[::1] == s[::-1]:
    print(1)
else:
    print(0)