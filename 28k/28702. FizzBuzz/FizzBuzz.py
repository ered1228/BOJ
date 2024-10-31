a = str(input())
b = str(input())
c = str(input())

A = [a, b, c]
inx = []
for i in range(3):
    if A[i] != 'Fizz' and A[i] != 'Buzz' and A[i] != 'FizzBuzz':
        A[i] = int(A[i])
        inx.append(i)

if max(inx) == 0:
    temp = A[0] + 3
elif max(inx) == 1:
    temp = A[1] + 2
else:
    temp = A[2] + 1

if temp % 3 == 0 and temp % 5 == 0:
    print('FizzBuzz')
elif temp % 3 == 0:
    print('Fizz')
elif temp % 5 == 0:
    print('Buzz')
else:
    print(temp)