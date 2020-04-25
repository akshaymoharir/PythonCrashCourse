
## Python Crash Course

# Exercise 4.2: Animals:  
#               Think of at least three different animals that have a common characteristic. 
#               Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#               • Modify your program to print a statement about each animal, such as A dog would make a great pet.
#               • Add a line at the end of your program stating what these animals have in common. 
#               You could print a sentence such as Any of these animals would make a great pet!

def main():
    
    # Animals with a common characteristic
    animals = ["Sheep", "Camel", "Dear"]

    # Print name of each animal
    print("\nAnimals with a common characteristic are: ")
    for animal in animals:
        print(animal)

    # Print a statement about each animal
    print("\nPrinting a sentence about each animal:")
    for animal in animals:
        print(animal + " eats vegetarian food.")
    
    # Print a common characteristic about these animals
    print("\nA common characteristic these animals have is they drink water by their mouth, they suck in water while drinking!!\n")

if __name__ == '__main__':
    main()

