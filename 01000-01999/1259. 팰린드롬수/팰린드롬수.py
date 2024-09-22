while True:
    n = input()
    if n == '0':
        break
    if n[::1] == n[::-1]:
        print('yes')
    else:
        print('no')