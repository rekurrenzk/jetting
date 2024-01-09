#logical operators (and, or, not) are used to check if two or more
    #conditional statements are true or not



temp = input('what is the temperature outside?')
temp = int(temp)
if temp>= 0 and temp <= 15:
    print('it is cold outside'
          'YOU MUST GO AND SWIM ON THE BOSPHOROUS')

elif temp>= 15 and temp <= 25:
    print('I would not say weather is bad but meh')

elif temp >= 25 and temp <=31:
    print('still meh. you do you')

elif temp < 0 or temp >=31:
    print('CHALLANGE MOD. LET GOOOOOOOOOOOO')

else: # no use case
    print('wtf is this')

