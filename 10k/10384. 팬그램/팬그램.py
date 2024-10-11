import sys
input = sys.stdin.readline

def pangram(word, i):
    A = [0]*26
    for w in word:
        if ord(w) >= 97 and ord(w) <= 122:
            A[ord(w)-97] += 1
    res = min(A)
    if res == 1:
        print(f"Case {i}: Pangram!")
    elif res == 2:
        print(f"Case {i}: Double pangram!!")
    elif res == 3:
        print(f"Case {i}: Triple pangram!!!")
    else:
        print(f"Case {i}: Not a pangram")
    

t = int(input())
for i in range(1, t+1):
    word = str(input().strip())
    word = word.lower()
    pangram(word, i)