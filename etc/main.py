
def mark():
    print("$")
    return


def asking():

    ingredients_price = {
        "milk": 2,
        "espresso": 2.5,
        "chocolate": 5,
        "water": 1,
        "sugar": 1.25

    }

    print(coffe.keys())

    your_coffe = input("which coffe would you like to have? ")

    for your_coffe in coffe.keys():

        def ingredient():

            ask1 = input("would you like to have an extra ingredients? ")
            if ask1 == "yes":

                print("choose only one ingredient: ")

            print(ingredients_price.keys(), "\n")
            print(ingredients_price.values(), "prices")

            for ingredients in ingredients_price.keys():

                ingredients = input()
                total_ingredient = {"your coffe"}
                total_ingredient = ingredients.update("your coffe")
                print("your ingredients are: ", total_ingredient)

                return total_ingredient

            if ask1 == "no":

                print("done")

            else:

                print("your choice is incorrect")
                return ingredient()

        ingredient()

    return


coffe = {
    "latte ": ["milk", "espresso", "sugar"],
    "espresso ": ["espresso"],
    "americano ": ["water", "espresso"],
    "mocha ": ["chocolate","espresso", "milk"]
}

asking()