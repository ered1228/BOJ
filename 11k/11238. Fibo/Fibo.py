import math
def matrix_multi_2by2(A, B):
    Mat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                Mat[i][j] += A[i][k] * B[k][j]
                Mat[i][j] %= 10**9 + 7
    return Mat

def matrix_pow(Mat, n):
    I = [[1, 0], [0, 1]]
    base = Mat
    while n > 0:
        if n % 2 == 1:
            I = matrix_multi_2by2(I, base)
        base = matrix_multi_2by2(base, base)
        n //= 2
    return I

Mat = [[1, 1], [1, 0]]
MOD = 10**9 + 7
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = math.gcd(n, m)
    if g == 1:
        print(1)
    else:
        fn = matrix_pow(Mat, g-1)[0][0]
        print(fn % MOD)