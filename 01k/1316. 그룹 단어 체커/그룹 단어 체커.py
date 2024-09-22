import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for _ in range(n):
    word = str(input())
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            continue
        elif word[i-1] in word[i:]:
            cnt -= 1
            break
print(cnt)   