import sys
input = sys.stdin.readline

card = {}
n = int(input())
for _ in range(n):
    c = int(input())
    if c in card:
        card[c] += 1
    else:
        card[c] = 1

res = sorted(card.items(), key = lambda x : (-x[1], x[0]))
print(res[0][0])