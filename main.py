print("let us do the counting")

text = ("in mathematics and computer science an algorithm is a "
        "finite sequence of rigorous instructions typically "
        "used to solve a class of specific problems or to "
        "perform computation algorithms are used as specifications "
        "for performing calculations and data processing more "
        "advanced algorithms ")

counted = text.lower().split(' ')
print("\n", ">>total words in the text is:", len(counted))

print("\n\nlets sort the text")

sorty = sorted(counted)
counts = dict(
)

for word in counted:
    counts[word] = counts.get(word, 0) + 1
    final = counts[word]
    print(word, final)
