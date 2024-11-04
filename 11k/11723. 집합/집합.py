import sys
input = sys.stdin.readline

S = set()
n = int(input())
for _ in range(n):
    s = input().rstrip().split()
    if s[0] == 'add':
        S.add(int(s[1]))
    elif s[0] == 'remove':
        S.discard(int(s[1]))
    elif s[0] == 'check':
        if int(s[1]) in S:
            print(1)
        else:
            print(0)
    elif s[0] == 'toggle':
        if int(s[1]) in S:
            S.discard(int(s[1]))
        else:
            S.add(int(s[1]))
    elif s[0] == 'all':
        S = set(range(1, 21))
    else:
        S.clear()