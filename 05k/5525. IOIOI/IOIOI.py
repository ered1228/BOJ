n = int(input())
l = int(input())
s = str(input())
p = 'IOI'
o_cnt, i, res = 0, 0, 0

while i+3 <= l:
    if s[i:i+3] == p:
        o_cnt += 1
        if o_cnt == n:
            res += 1
            o_cnt -= 1
        i += 2
    else:
        o_cnt = 0
        i += 1

print(res)