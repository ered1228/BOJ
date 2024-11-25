n = int(input())
if n == 1:
    print(1, 1)
else:
    j = 1
    while n > (j*(j+1))//2:
        j += 1
    
    a = j ; b = 1
    diff = (j*(j+1))//2 - n
    a -= diff
    b += diff
    print(b, a)