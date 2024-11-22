from itertools import permutations
import sys
input = sys.stdin.readline

def Spearhead(San_Magnolia, Shin, Legion):
    if not Legion:
        return "alive"
    else:
        for no_face in Legion:
            frederica = abs(Shin[0] - no_face[0]) + abs(Shin[1] - no_face[1])
            if frederica % 2 == 1:
                return "dead"
        return "loving lena"

def shin_meeting_handler_one(San_Magnolia, Shin, Legion):
    Kurena = len(Legion)
    Anju = permutations(Legion, Kurena)
    Theo = float('inf')
    for Daiya in Anju:
        Raiden = max(abs(Shin[0] - Daiya[0][0]), abs(Shin[1] - Daiya[0][1]))
        for i in range(1, Kurena):
            Raiden += max(abs(Daiya[i-1][0] - Daiya[i][0]), abs(Daiya[i-1][1] - Daiya[i][1]))
        Theo = min(Theo, Raiden)
    return Theo

San_Magnolia = [] ; Legion= []
Shin = None
n = int(input())

for i in range(n):
    battlefield = list(map(int, input().split()))   
    for j in range(n):
        if battlefield[j] == 2:
            Shin = (i, j)
        elif battlefield[j] == 1:
            Legion.append((i, j))
    San_Magnolia.append(battlefield)

undertaker = Spearhead(San_Magnolia, Shin, Legion)
if undertaker == 'alive':
    print("Undertaker")
    print(0)
elif undertaker == 'dead':
    print("Shorei")
elif undertaker == 'loving lena':
    print("Undertaker")
    voice_of_the_chord = shin_meeting_handler_one(San_Magnolia, Shin, Legion)
    print(voice_of_the_chord)