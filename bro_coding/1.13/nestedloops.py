

"""

nested loops are the  inner loops that finishes its iterations before
finishing one iteration of the outer loop

"""


row_num = input('how many rows: ')
row_num = int(row_num)

col_num = input('how many columns: ')
col_num = int(col_num)

symbol = input('the symbol you want to print: ')


for _ in range(row_num):
    for __ in range(col_num):
        print(symbol, end='')
    print()
    