import sys
input = sys.stdin.readline

def count(s):
    res = [0, 0]
    if s == s[::-1]:
        res = [1, (len(s)//2)+1]
    else:
        res[0] = 0
        for i in range(1, len(s)):
            if s[i-1] != s[-i]:
                res[1] = i
                break
    return res

t = int(input())
for _ in range(t):
    s = str(input().strip())
    res = count(s)
    print(res[0], res[1])