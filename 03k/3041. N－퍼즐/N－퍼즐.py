puzzle = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', '.']]
test = []
dist = 0

def f(temp, puzzle):
    d = 0
    for k in range(4):
        for l in range(4):
            if puzzle[k][l] == temp:
                d += abs(i - k) + abs(j - l)
                return d

for _ in range(4):
    s = input()
    li = []
    for m in range(4):
        li.append(s[m])
    test.append(li)

for i in range(4):
    for j in range(4):
        temp = test[i][j]
        if temp != '.':
            dist += f(temp, puzzle)
print(dist)