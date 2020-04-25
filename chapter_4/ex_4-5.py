
## Python Crash Course

# Exercise 4.5: Summing a Million:
#               Make a list of the numbers from one to one million, 
#                   and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#               Also, use the sum() function to see how quickly Python can add a million numbers.


def main():

    # Prepare list of one million numbers
    listOfOneMillionNumbers = list(range(1,1000001))
   

    # Print min and max of the list
    minOfList = min(listOfOneMillionNumbers)
    print("\nPrinting minimum number from the list:", minOfList)
    maxOfList = max(listOfOneMillionNumbers)
    print("\nPrinting maximum number from the list:", maxOfList)

    # Print sum of the list
    sumOfList = sum(listOfOneMillionNumbers)
    print("\nSum of the list is: ", sumOfList, "\n")

if __name__ == '__main__':
    main()

