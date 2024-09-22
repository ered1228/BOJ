def fac(x):
    if x == 0:
        result = 1
    else:
        result = 1
        for i in range(1, x+1):
            result *= i
    return result

n = int(input())
print(fac(n))