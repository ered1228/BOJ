while True:
    try:
        n = int(input())
        lena = 1
        shin = 1
        if n == 1:
            print(1)
        else:
            while lena % n != 0:
                lena = lena*10 + 1
                shin += 1
            print(shin)
    except:
        break