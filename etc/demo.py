"""def is_leap(year):
    leap = False
    not_leap = True

    year_read = year


    conds1 = (year_read % 4) == 0
    conds2 = (year_read % 100) == 0
    conds3 = (year_read % 400) == 0

    # Write your logic here
    if conds1 is True and conds2 is True and conds3 is True:
        return not_leap

    elif conds1 is True and conds2 is True and conds3 is False:
        return leap


    elif conds1 is True and conds2 is False and conds3 is True:
        return not_leap

    elif conds1 is False and conds2 is False and conds3 is False:
        return leap

    elif conds1 is True and conds2 is False and conds3 is False:
        return not_leap

    else:
        return

year = int(input())
print(is_leap(year))"""

############################
"""
n = 5

for _ in range(n):
    a = _ + 1
    print(a, end="")"""


##################

"""
n = int(input())


def solver(n_cal):
    n_even = 0
    n_odd = 1
    n_cal = n
    if int(n % 2) == n_odd:
        print("weird")


    else:
        if int(n % 2) == n_even and n in range(2, 5):
            print("Not Weird")

        elif int(n % 2) == n_even and n in range(6, 21):
            print("Weird")

        elif int(n % 2) == n_even and (n > 20):
            print("Not Weird")
        else:
            return


solver(n)
"""
#########################
"""
a = int(input())
b = int(input())


def solver(a, b):
    aVal = int(a)
    bVal = int(b)
    condition = 1 <= aVal <= 10**10 and 1 <= bVal <= (10 ** 10)
    conditionSt = bool(condition)

    if conditionSt == "True":
        firstContainer = int(aVal + bVal)
        secondContainer = int(aVal - bVal)
        thirdContainer = int(aVal * bVal)

        print(firstContainer)
        print(secondContainer)
        print(thirdContainer)


    else:
        return solver(a, b)


solver(a, b)"""


######################

x = 3
y = 2
z = 2
n = 3 #gives the permutation rate


def leader(x, y, z, n):

    # list comprehension

    # iterativeFunc = [x, y, z for in range(n)]

    pr_x = [_ for _ in range(x)]
    pr_y = [__ for __ in range(y)]
    pr_z = [___ for ___ in range(z)]

    pr_all = pr_x, pr_y, pr_z

    myResult = [pr_all * i for i in range(n)]

    print(myResult, end="")


leader(x, y, z, n)

"""
q = 4
b= 3
n=2

for _ in range(q):

    print(_)
"""
