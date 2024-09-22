import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #n은 카드 개수
card = list(map(int, input().split()))
s = -1

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = card[i] + card[j] + card[k]
            if temp <= m and temp > s:
                s = temp

print(s)