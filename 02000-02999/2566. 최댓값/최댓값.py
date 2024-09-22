B = []
for _ in range(9):
    A = list(map(int, input().split()))
    B.extend(A)
value = max(B)
temp = B.index(value) + 1
if temp % 9 != 0:
    raw = (temp // 9) + 1
    column = (temp % 9)
else:
    raw = (temp // 9)
    column = 9
print(value)
print(raw, column, end=" ")