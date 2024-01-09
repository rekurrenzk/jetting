
# while loop is a statement that will execute its block of code while cond remains true


name = ''

while len(name)==0:
    name=input('enter your name: ')

print(f'welcome {name}')


nick = ''

while not nick:
    print('please enter your nick')
    nick = input()
print(f'welcome {nick}')

