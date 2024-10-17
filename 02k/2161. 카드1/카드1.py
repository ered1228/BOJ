n = int(input())
card = [i for i in range(1, n+1)]
res = []

while True:
    res.append(card.pop(0))
    if len(card) > 1:
        card.append(card.pop(0))
    elif len(card) == 1:
        res.append(card[0])
        break
    else:
        break

for r in res:
    print(r, end=" ")