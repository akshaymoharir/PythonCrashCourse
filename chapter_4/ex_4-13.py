
## Python Crash Course

# Exercise 4.12: Buffet: 
#                A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#                   • Use a for loop to print each food the restaurant offers.
#                   • Try to modify one of the items, and make sure that Python rejects the change.
#                   • The restaurant changes its menu, replacing two of the items with different foods. 
#                   Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

def main():

    # Five basic food that restaurant offers
    foodItems = ("Idli Sambar", "Chhole Bature", "Samosa", "Kachori", "Upma")

    # Print restaurant menu
    print("\nRestaurant menu: ")
    for foodItem in foodItems:
        print(foodItem)

    # Try to change one foodItem
    # Commenting following line after testing that python doesn't allow to 
    #   change item in tuple
    # Error observed: TypeError: 'tuple' object does not support item assignment
    # foodItems[2] = "Aloo Paratha" 
    

    # Change restaurant menu, replace 2 food items with different food
    foodItems = (foodItems[0], foodItems[1], "Paratha", "Misal Pav", 
    foodItems[2])

    # Print restaurant menu
    print("\nRestaurant menu after replacing 2 food items: ")
    for foodItem in foodItems:
        print(foodItem)

    print("\n")


if __name__ == '__main__':
    main()

