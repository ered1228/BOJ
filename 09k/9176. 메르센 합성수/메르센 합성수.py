import math

def prime_factor(x):
    factor = [x, 1]
    is_prime = True
    for i in range(3, int(math.sqrt(x)+1), 2):
        if x % i == 0:
            exp = 1
            x //= i
            is_prime = False
            while x % i == 0:
                exp += 1
                x //= i
            factor = [i, exp]
            break
    return factor, x, is_prime

k = int(input())
not_prime = [11, 23, 29, 37, 41, 43, 47, 53, 59]
prime = {2, 3, 5, 7, 13, 17, 19, 31, 61}
M = []

for p in not_prime:
    if p <= k:
        temp = ((2**p)-1)
        temp_f, resi, is_prime = prime_factor(temp)
        M.append(temp_f[0])
        while is_prime == False:
            temp_f, resi, is_prime = prime_factor(resi)
            if not is_prime: 
                M.append(temp_f[0])
            else:
                M.append(resi)
    
        res = " * ".join(map(str, M))
        print(res, end="")
        print(f" = {temp} = ( 2 ^ {p} ) - 1")
        M = []