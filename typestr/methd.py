def ret():
    nonofyour = str.casefold("Привет, как дела?")
    width = len(nonofyour) + 2
    fillchar = '|'
    res = nonofyour.center(width, fillchar)
    print(res)


ret()

def ret2():
    print()
    print('this is ret2')
    a = input(' any name you want: ')
    lim = '|'
    if a:
        outa = a.center(len(a)+2, lim)
        print(outa)
    else:
        pass


ret2()


def nol():
    text = 'zkvernturelab'
    if text:
        for char in set(text):
            count = text.count(char)
            print(f'{char}: {count}')


nol()


def trns():
    inp = "اءَكَ مِنَ الْعِلْمِۙ مَا لَكَ مِنَ اللّٰهِ مِنْ وَلِيٍّ وَلَا وَاق"

    table_trans = str.maketrans('', '')
    translated = inp.translate(table_trans)
    print(translated.isascii())
    if translated.isprintable():
        return True
    else:
        return False


trns()


def rempre(sentence):

    if sentence.startswith('ال'):
        return sentence[2:]
    else:
        return sentence


arabic_sth = "اءَكَ مِنَ الْعِلْمِۙ مَا لَكَ مِنَ اللّٰهِ مِنْ وَلِيٍّ وَلَا وَاق"

modified_sentence = rempre(arabic_sth)


print(modified_sentence)
