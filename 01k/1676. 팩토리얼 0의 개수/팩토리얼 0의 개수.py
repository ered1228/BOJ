from math import factorial
n = int(input())
temp = 0
N = factorial(n)
while True:
    if N % 10 == 0:
        N = N // 10
        temp += 1
    else:
        break
print(temp)