

"""

loop control statements are executions to be changed from its
normal sequences

break -- used to terminate the loop entirely
continue -- skips to the next iteration of the loop
pass -- does nothing, acting as a placeholder

"""
while True:
    name = input('please type your name:')
    if name != '':
        print(f'welcome {name}')
        break
    else:
        continue

phone_num = "123-456-789"

for i in phone_num:
    if i == '-':
        continue
    print(i, end='')


for i in range(1,21):
    if i == 13:
        pass
    else:

        print(i)


