n = int(input())
word = str(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
N = []

for i in range(26):
    N.append(word.count(alpha[i]))
             
rs = max(N)
ix = N.index(max(N))
print(alpha[ix], rs)