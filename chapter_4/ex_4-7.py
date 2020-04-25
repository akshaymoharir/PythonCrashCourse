
## Python Crash Course

# Exercise 4.7: Threes:  
#               Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list.


def main():

    # Prepare list of multipliers of 3 from 3 to 30
    listOfMultipliersOfThree = [3*value for value in range(1,11)]

    # For loop to print numbers in the list
    print("\nPrinting multipliers of 3 from 3 to 30:")
    for number in listOfMultipliersOfThree:
        print(number)
    
    # Print number of items in the list
    print("\nThere are", len(listOfMultipliersOfThree), "multipliers of 3 in 3 to 30. \n")

if __name__ == '__main__':
    main()

