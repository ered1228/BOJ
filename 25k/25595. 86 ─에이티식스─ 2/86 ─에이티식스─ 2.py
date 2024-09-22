import sys
input = sys.stdin.readline

# 오랜만입니다, 핸들러 원.

battlefield = int(input())
shin = []
Legion = []
avid = True

for i in range(battlefield):
    L = list(map(int, input().split()))
    for j in range(battlefield):
        if L[j] == 1:
            Legion.append([i, j])
        elif L[j] == 2:
            shin = [i, j]

if not Legion:
    print('Lena')
else:
    for no_face in Legion:
        frederica = abs(shin[0] - no_face[0]) + abs(shin[1] - no_face[1])
        if frederica % 2 == 0:
            avid = False
            break
    if avid:
        print('Lena')
        # whisper your name again
        # then restart it right away
    else:
        print('Kiriya')