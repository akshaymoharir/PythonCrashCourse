
## Python Crash Course

# Exercise 4.11: My Pizzas, Your Pizzas: 
#                Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. 
#                Then, do the following:
#                   • Add a new pizza to the original list.
#                   • Add a different pizza to the list friend_pizzas.
#                   • Prove that you have two separate lists. 
#                       Print the message, My favorite pizzas are:, and then use a for loop to print the first list. 
#                       Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
#                       Make sure each new pizza is stored in the appropriate list.

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
    friend_pizzas = myFavoritePizzas[:]

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

