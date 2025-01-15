import math

def pal(k):
    if k == 1:
        return [str(i) for i in range(10)]
    elif k == 3:
        res = []
        for i in range(10):
            for j in range(10):
                res.append(str(i) + str(j) + str(i))
        return res
    else:
        res = []
        temp_pal = pal(k-2)
        for i in range(10):
            for tp in temp_pal:
                res.append(str(i) + tp + str(i))
        return res

def prime_judge(n):
    for div in range(3, int(math.sqrt(n))+1, 2):
        if n % div == 0:
            return False
    return True

a, b = map(int, input().split())
prime = [2, 3, 5, 7, 11]
end_num = ['1', '3', '7', '9']

l = len(str(b))-2
for i in range(1, l+1, 2):
    A = pal(i)
    for ed in end_num:
        for aa in A:
            temp = ed + aa + ed
            temp = int(temp)
            if prime_judge(temp):
                prime.append(temp)

for p in prime:
    if a <= p <= b:
        print(p)
print(-1)
