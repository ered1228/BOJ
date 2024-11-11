D = list(map(int, input().split()))
idx = D.index(20)

if idx == 0:
    alice = (20 + D[19] + D[1]) / 3
elif idx == 19:
    alice = (20 + D[18] + D[0]) / 3
else:
    alice = (D[idx-1] + 20 + D[idx+1]) / 3

bob = 210 / 20

if alice > bob:
    print('Alice')
elif alice == bob:
    print('Tie')
else:
    print('Bob')