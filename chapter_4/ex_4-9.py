
## Python Crash Course

# Exercise 4.9: Cube Comprehension:  
#               Use a list comprehension to generate a list of the first 10 cubes.


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

