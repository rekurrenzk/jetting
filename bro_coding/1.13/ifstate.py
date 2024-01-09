# if statement is a block of code that will execude if its condition is true

# it is a one way of decision making in programming

age = int(input('whats your age?: '))

if 0<age < 18:
    print('you are not allowed to get in!')
elif 18<=age<=22:
    print('you are only allowed to join in Europe Channel!')
elif age < 0:
    print('you joking right?')
else:
    print('you are free to enter!')



