while True:
    parity = str(input())
    if parity == '#':
        break
    else:
        cnt = parity.count('1')
        bitmask = parity[-1]
        parity = parity[:-1]
        if cnt % 2 == 0 and bitmask == 'e':
            parity += '0'
        elif cnt % 2 == 0 and bitmask == 'o':
            parity += '1'
        elif cnt % 2 == 1 and bitmask == 'e':
            parity += '1'
        else:
            parity += '0'
    print(parity)