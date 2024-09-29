n = int(input())
MOD = 10**9 + 7

def matrix_pow_2(A, B):
    R = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                R[i][j] += A[i][k] * B[k][j]
                R[i][j] %= MOD
    return R

def fibo(n):
    I = [[1, 0], [0, 1]]
    base = [[1, 1], [1, 0]]
    while n > 0:
        if n % 2 == 1:
            I = matrix_pow_2(I, base)
        base = matrix_pow_2(base, base)
        n //= 2
    return I
        
if n <= 2:
    print(1)
else:
    print(fibo(n-1)[0][0] % MOD)