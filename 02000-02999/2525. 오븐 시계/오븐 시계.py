a, b = map(int, input().split())
c = int(input())
result_h = 0
result_m = 0
d = 0
if ((60*a)+b+c) < 1440:
    result_h = ((60*a)+b+c)//60
    result_m = ((60*a)+b+c)%60
elif ((60*a)+b+c) == 1440:
    result_h = 0
    result_m = 0
else:
    d = ((60*a)+b+c)-1440
    result_h = d//60
    result_m = d%60
print(result_h, result_m)