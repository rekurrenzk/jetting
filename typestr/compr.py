from time import sleep

for second in range(3, 0, -1):
    print(second, end=" ", flush=True)
    sleep(0.5)

print('\nLets GOOO!')




def ret():
    this = [x*x for x in [1, 2, 3, 4]]
    return this


print(ret())


def ret2():
    this = [x*x for x in range(1, 10, 2)]
    return this


print(ret2())

def ret3():
    this = [(x, x*x) for x in range(10)]
    return this


print(ret3())


def ret4():
    this = [x for x in range(0, 10) if (x % 2 == 0)]
    return this


print(ret4())


def ret5():
    this = [x*x*x for x in range(0, 20)]
    return this


t = ret5()
print(t)




print('_-_-_-_-_-_-_-_-_-_-_-_-_-', end='\n', flush=True)

def ret6():
    prename = 'TestHook-en'
    sufname = 'methylphenidate'

    return prename.removeprefix('Test'), sufname.removesuffix('phenidate'),\
        prename.removeprefix('Hook') # this will not return


t = ret6()
print(t)


def ret7():
    this = '    remember what the dormous said'
    print(this.lstrip())
    print(this.lstrip('remember'))
    print(this.lstrip('     remember'))
    print(this.replace('dormous', 'fatih'))
    print(this)


ret7()

'''
str.rindex(sub[, start[,end]])
'''


