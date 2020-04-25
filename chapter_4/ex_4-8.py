
## Python Crash Course

# Exercise 4.8: Cubes:  
#               A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#               Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#                   and use a for loop to print out the value of each cube .


def main():

    # Prepare list of cubes of numbers from 1 to 10
    listOfCubes = [number**3 for number in range(1,11)]

    # For loop to print numbers in the list
    print("\nPrinting cubes of numbers from 1 to 10:")
    for idx in range(len(listOfCubes)):
        print("Cube of", idx+1, "is:", listOfCubes[idx])
    
    print("\n")

if __name__ == '__main__':
    main()


