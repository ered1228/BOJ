def moving(king, stone, x, y):
    temp_king, temp_stone = None, None
    temp_king = (ord(king[0]) + x, int(king[1]) + y)
    temp_stone = (ord(stone[0]) + x, int(stone[1]) + y)
    if temp_king != (ord(stone[0]), int(stone[1])):
        if 64 < int(temp_king[0]) < 73 and 0 < temp_king[1] < 9:
            return chr(temp_king[0])+str(temp_king[1]), stone
        else:
            return king, stone
    else:
        if 64 < int(temp_stone[0]) < 73 and 0 < temp_stone[1] < 9:
            return chr(temp_king[0])+str(temp_king[1]), chr(temp_stone[0])+str(temp_stone[1])
        else:
            return king, stone

king, stone, n = input().split()
moves = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
        'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

for _ in range(int(n)):
    move = str(input())
    king, stone = moving(king, stone, moves[move][0], moves[move][1])
print(king)
print(stone)