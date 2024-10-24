import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
hello = set()
for _ in range(n):
    chat = str(input().strip())
    if chat == 'ENTER':
        cnt += len(hello)
        hello.clear()
    else:
        hello.add(chat)

cnt += len(hello)
print(cnt)