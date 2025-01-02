from itertools import permutations, combinations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
card = [] ; cardset = set()
for _ in range(n):
    card.append(int(input()))

choose = combinations(card, k)
for cs in choose:
    temp = permutations(list(cs), k)
    for c in temp:
        res = ''
        for cc in c:
            res += str(cc)
        cardset.add(res)

print(len(cardset))