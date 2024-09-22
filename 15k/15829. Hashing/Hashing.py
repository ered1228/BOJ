n = int(input())
s = str(input())
hash_value = 0

for i in range(n):
    a = ord(s[i]) - 96
    r = 31**i
    hash_value += (a*r)
if hash_value >= 1234567891:
    hash_value = hash_value % 1234567891
print(hash_value)