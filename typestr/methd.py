def ret():
    nonofyour = str.casefold("Привет, как дела?")
    width = len(nonofyour)
    width += 2
    fillchar = '|'
    res = nonofyour.center(width, fillchar)
    print(res)


ret()

def ret2():
    a = input(' any name you want: ')
    lim = '|'
    if a:
        outa = a.center(len(a)+2, lim)
        print(outa)
    else:
        pass


ret2()


def nol():
    a = 'zkvernturelab'
    if a:
        for char in set(a):
            count = a.count(char)
            print(f'{char}: {count}')

nol()


