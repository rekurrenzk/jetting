"""

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""
name = '       format_string at the glance'
name = name.strip()
print(name)

name_c = name.capitalize()
print(name_c)

name_u = name.upper()
print(name_u)

name_t = name.title()
print(name_t)


new_name = input('your full name: ').split().__str__().title()


first, last = new_name.split(" ")
print(f'hello, ', new_name)