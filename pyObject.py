

# Data Structures # check out the py docs!

# objects make use of each other's capabilities
# an object is a bit of self-contained code and data



# Some Definitions:

    # Class - a template - Dog
    # Method/Message - A defined capability of a class - bark()
    # Field or attribute - A bit od data in a class - length
    # Object or Instance - A particular instance of a class - Lassie
        # instance is the actual object created at runtime.
"""

class PartyAnimal:

    x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)


an = PartyAnimal()

an.party()
an.party()
"""

# the dir() command lists capabilities
"""dir(an)"""

# Object LifeCyle #

    # constructor: to set up some instance variables to have the proper
                        #initial values when the object is created

ListColor = ["blue", "green", "red"]
ListBrand = ["BMW", "Mercedes", "Fiat"]
ListYear = []
count = 0



class Cars:
    def __init__(self, *args):
        attributes = ['color', 'brand', 'year']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

        for attr in attributes[len(args):]:
            setattr(self, attr, "not defined")

    def match(self):
        print(f"{self.color}, {self.brand}, {self.year}")

Xcars = Cars(ListColor, ListBrand, ListYear)

Xcars.match()