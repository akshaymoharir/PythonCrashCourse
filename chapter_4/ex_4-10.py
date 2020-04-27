
## Python Crash Course

# Exercise 4.10: Slices:  
#               Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#               • Print the message, The first three items in the list are: 
#                   . Then use a slice to print the first three items from that program’s list .
#               • Print the message, Three items from the middle of the list are: 
#                   . Use a slice to print three items from the middle of the list .
#               • Print the message, The last three items in the list are: 
#                   . Use a slice to print the last three items in the list .


def main():

    # Prepare list of cubes of numbers from 1 to 10
    listOfCubes = [number**3 for number in range(1,11)]

    # For loop to print numbers in the list
    print("\nPrinting cubes of numbers from 1 to 10:")
    for idx in range(len(listOfCubes)):
        print("Cube of", idx+1, "is:", listOfCubes[idx])
    
    ############## End of Previos exercise #############################

    # Print The first three items in the list are:
    print("\nFirst three elements in the above list:", listOfCubes[0:3])


    # Print The middle three items in the list are:
    print("\nMiddle three elements in the above list:", listOfCubes[3:6])

    # Print The last three items in the list are:
    print("\nLast three elements in the above list:", listOfCubes[-3:])
    
    print("\n")


if __name__ == '__main__':
    main()

