
def ret():
    this = [x*x for x in [1,2,3,4]]
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
    this = [x for x in range(0,10) if (x % 2 == 0)]
    return this


print(ret4())