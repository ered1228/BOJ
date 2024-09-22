n = int(input())
f = int(input())

temp1 = n // 100
temp2 = temp1 * 100

while temp2 % f != 0:
    temp2 += 1
temp2 = str(temp2)
print(temp2[-2:])