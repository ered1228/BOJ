h, m = map(int,input().split())
result_h = 0
result_m = 0
if m >= 45:
    result_h = h
    result_m = m-45
else:
    if h > 0:
        result_h = h-1
        result_m = m+15
    else:
        result_h = 23
        result_m = m+15
print(result_h, result_m)