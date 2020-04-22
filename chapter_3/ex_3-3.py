
## Python Crash Course

# Exercise 3.3: Your Own List: 
#               Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#               Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.” 

def main():
    cars = ['Accord', 'Altima']
    print("I used to drive", cars[1].title())
    print("I am driving ", cars[0].title(), "now! I love Honda", cars[0].title(), "!!")

if __name__ == '__main__':
    main()

