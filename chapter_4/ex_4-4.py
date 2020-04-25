
## Python Crash Course

# Exercise 4.4: One Million:  
#               Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#               (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)


def main():

    # Prepare list of one million numbers
    listOfOneMillionNumbers = list(range(1,1000001))
    listOfEleven = [value for value in range(1,12)]

    # For loop to print numbers from 1 to 1000000
    print("\nPrinting numbers from 1 to 1000000:")
    for number in listOfOneMillionNumbers:
        print(number)

    # For loop to print numbers from 1 to 11
    print("\nPrinting numbers from 1 to 11:")
    for num in listOfEleven:
        print(num)

if __name__ == '__main__':
    main()

