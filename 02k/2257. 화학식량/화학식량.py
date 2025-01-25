molecule = str(input())
nums ={'2', '3', '4', '5', '6', '7', '8', '9'}
atom = {'H': 1, 'C':12, 'O': 16}
stack = []
temp = []

for m in molecule:
    if m in atom:
        stack.append(atom[m])
    elif m in nums:
        tail = stack.pop()
        stack.append(tail*int(m))
    elif m == '(':
        stack.append(m)
    elif m == ')':
        for s in range(len(stack)-1, -1, -1):
            if stack[s] != '(':
                temp.append(stack.pop())
            else:
                stack.pop() #removing '('
                stack.append(sum(temp))
                temp.clear()
                break

print(sum(stack))