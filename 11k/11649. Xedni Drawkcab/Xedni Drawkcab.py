n = int(input())
card = []
for _ in range(n):
    card.append(str(input())[::-1])
card.sort()
for c in card:
    print(c)