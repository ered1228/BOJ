import math

def is_prime(n):
    if n == 1:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

s = str(input())
res = 0
for i in range(len(s)):
    temp = s[i].lower()
    if s[i] == temp:
        res += ord(s[i]) - 96
    else:
        res += ord(s[i]) - 38
if is_prime(res):
    print("It is a prime word.")
else:
    print("It is not a prime word.")