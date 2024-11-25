import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = {}
for _ in range(n):
    a, b = map(str, input().rstrip().split())
    password[a] = b
for _ in range(m):
    site = str(input().rstrip())
    print(password[site])