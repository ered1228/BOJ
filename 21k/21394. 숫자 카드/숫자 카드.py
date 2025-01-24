from collections import deque

t = int(input())
for _ in range(t):
    card = list(map(int, input().split()))
    card[8] += card[5]
    card[5] = 0
    card = enumerate(card, start=1)
    card = sorted(card, key=lambda x: -x[0])
    C = [] ; st = [] ; ed = deque([])
    for idx, val in card:
        C += [idx]*val
    s = True
    for c in C:
        if s:
            st.append(c)
        else:
            ed.appendleft(c)
        s = not s
    print(' '.join(map(str, st+list(ed))))