burger, side, beverage = map(int, input().split())
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

res1 = sum(B) + sum(C) + sum(D)
sale = 0

B.sort(reverse = True)
C.sort(reverse = True)
D.sort(reverse = True)

re = min(burger, side, beverage)
for i in range(re):
    sale += (B[i] + C[i] + D[i]) * 0.1

print(res1)
print(int(res1 - sale))