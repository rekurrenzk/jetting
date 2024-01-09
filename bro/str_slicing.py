
"""
slicing is creating a substring by extracting elem from another string
"""
name = 'rekurrenzk'
first_name = name[3]

print(first_name)
print(name[3])
print(name[5])
print(name[1:4])
print(name[0:4:2])
print(name[:-3])
print(name[-1])

# [start:stop:step]

funky = name[::]
print(funky)
reverse_funky = name[::-1]
print(reverse_funky)

website_url = 'http://www.rekurrenzk.com'
slice = slice(7,-1)

print(website_url[slice])



