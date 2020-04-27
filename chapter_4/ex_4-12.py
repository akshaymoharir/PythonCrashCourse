
## Python Crash Course

# Exercise 4.12: More Loops: 
#                All versions of foods.py in this section have avoided using for loops when printing to save space.
#                Choose a version of foods.py, and write two for loops to print each list of foods.

def main():

    # My favorite pizzas
    myFavoritePizzas = ["Veg supreme", "Ultimate cheese lover's pizza", 
    "Pacific veggie"]

    # Print favorite pizzas
    print("My favorite pizzas are: ")
    for pizza in myFavoritePizzas:
        print(pizza)

    ################### End of Exercise 4.1 ############################

    # Make a copy of pizzas
    friend_pizzas = myFavoritePizzas.copy()

    # Add a pizza in the original list, myFavoritePizzas
    myFavoritePizzas.append("Margarita")

    # Add a different pizza in friend_pizzas
    friend_pizzas.append("Mexican herbs pizza")

    # Print my favorite pizzas
    print("\nMy favorite pizzas are: ")
    for pizza in myFavoritePizzas:
        print(pizza)

    # Print friend's favorite pizzas
    print("\nMy friend's favorite pizzas are: ")
    for pizza in friend_pizzas:
        print(pizza)


    print("\n")


if __name__ == '__main__':
    main()

