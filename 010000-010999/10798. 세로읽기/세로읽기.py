res = ''
word = []

for _ in range(5):
    w = str(input())
    word.append(w)
    
for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            res += word[j][i]
print(res)