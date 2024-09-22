A = []
num = 0
M = -2147483648

for i in range(9):
    a = int(input())
    A.append(a)

for j in range(9):
    if M < A[j]:
        M = A[j]
        num = j+1

print(M)
print(num)