A = []
B = []

for i in range(28):
    x = int(input())
    A.append(x)
    
for j in range(1, 31):
    if A.count(j) == 0:
        B.append(j)

B.sort()            
for b in B:
    print(b)