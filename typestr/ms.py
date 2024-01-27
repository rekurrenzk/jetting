

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


text = "Hello World!\rThis is a test string.\r\nIt contains different line breaks.\rCheck this out."

# Splitting the string into lines
lines = text.splitlines(keepends=True)
[print(line) for line in lines]
print()
print("hello\x85\nthis is me.\u2029this is where the magic starts")


for index, value in enumerate(['bing', 'bang', 'dong']):
    print(index, value)
print('_______________')
words = ['bing', 'bang', 'dong']

rev_word = list(reversed(words))

for i in range(len(words)):
    indx = len(words) - i
    val = rev_word[i]
    print(indx, val)
print("BUUM..!")
