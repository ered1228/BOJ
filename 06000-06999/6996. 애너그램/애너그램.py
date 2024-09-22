import sys
input = sys.stdin.readline

t = int(input())

def is_anagram(a, b):
    cnt = 0
    for i in range(len(a)):
        temp = a.count(a[i])
        temp2 = b.count(a[i])
        if temp != temp2:
            cnt += 1
    if cnt > 0:
        print("{} & {} are NOT anagrams.".format(a, b))
    else:
        print("{} & {} are anagrams.".format(a, b))

for _ in range(t):
    a, b = input().split()
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        print("{} & {} are NOT anagrams.".format(a, b))
    else:
        is_anagram(a, b)

# blather & reblath are anagrams.
# maryland & landam are NOT anagrams.
# bizarre & brazier are anagrams.