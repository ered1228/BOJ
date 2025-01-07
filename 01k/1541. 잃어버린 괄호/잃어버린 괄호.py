expression = str(input())
res = 0
operator = {'+', '-'}
temp = ''
seg = []
start = 0
first = True

for i in range(len(expression)):
    if expression[i] == '-':
        seg.append(expression[start:i])
        start = i+1
seg.append(expression[start:])

for eq in seg:
    semi_sum = 0
    for ex in eq:
        if ex not in operator:
            temp += ex
        else:
            semi_sum += int(temp)
            temp = ''
    if temp != '':
        semi_sum += int(temp)
        temp = ''
    
    if first:
        res += semi_sum
        first = False
    else:
        res -= semi_sum
    semi_sum = 0

print(res)