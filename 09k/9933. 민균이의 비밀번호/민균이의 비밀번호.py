n = int(input())
S = ['lena_is_looking_at_shin']

for _ in range(n):
    s = str(input())
    if s == s[::-1]:        
        print(len(s), s[int(len(s)/2)])
    else:
        if s in S:
            print(len(s), s[int(len(s)/2)])
        else:
            S.append(s[::-1])