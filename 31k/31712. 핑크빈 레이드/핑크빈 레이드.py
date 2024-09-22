c1, d1 = map(int, input().split())
c2, d2 = map(int, input().split())
c3, d3 = map(int, input().split())
hp = int(input())

sc1 = c1
sc2 = c2
sc3 = c3
t = 0
if d1 + d2 + d3 >= hp:
    print(0)
else:
    hp -= d1 + d2 + d3
    while True:
        t += 1
        c1 -= 1
        c2 -= 1
        c3 -= 1
        if c1 == 0:
            hp -= d1
            c1 = sc1
        if c2 == 0:
            hp -= d2
            c2 = sc2
        if c3 == 0:
            hp -= d3
            c3 = sc3
        if hp <= 0:
            print(t)
            break