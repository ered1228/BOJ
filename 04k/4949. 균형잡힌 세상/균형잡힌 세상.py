def f(sentense, stack):
    for i in range(len(sentense)):
        if sentense[i] == '(':
            stack.append(sentense[i])
        elif sentense[i] == '[':
            stack.append(sentense[i])
        elif sentense[i] == ')':
            if len(stack) == 0:
                return 'no'
            else:
                if stack[-1] == '[':
                    return 'no'
                else:
                    stack.pop()
        elif sentense[i] == ']':
            if len(stack) == 0:
                return 'no'
            else:
                if stack[-1] == '(':
                    return 'no'
                else:
                    stack.pop()
        else:
            pass
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'

while True:
    sentense = str(input())
    stack = []
    if sentense == '.':
        break
    else:
        print(f(sentense, stack))