
## Python Crash Course

# Exercise 4.6: Odd Numbers:  
#               Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#               Use a for loop to print each number.


def main():

    # Prepare list of odd numbers in 1 to 20
    listOfOddNumbers = list(range(1,21,2))

    # For loop to print numbers in the list
    print("\nPrinting odd numbers in the list:")
    for oddNum in listOfOddNumbers:
        print(oddNum)

    # Count numbers in the list
    print("\nThere are",len(listOfOddNumbers),"odd numbers in the list. \n")

if __name__ == '__main__':
    main()

