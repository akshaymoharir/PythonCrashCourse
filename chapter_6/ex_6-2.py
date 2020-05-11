
## Python Crash Course

# Exercise 6.2: Favorite Numbers:  
#               Use a dictionary to store people’s favorite numbers. 
#               Think of five names, and use them as keys in your dictionary. 
#               Think of a favorite number for each person, and store each as a value in your dictionary. 
#               Print each person’s name and their favorite number . 
#               For even more fun, poll a few friends and get some actual data for your program.
#


def exercise_6_2():

    print("\n")
    
    friends = {
                'Akshay':7,
                'Akash':9,
                'Yogesh':4,
                'Rahul':3
            }

    print("Akshay's favourite number:",friends['Akshay'])
    print("Rahul's favourite number:",friends['Rahul'])
    print("Yogesh's favourite number:",friends['Yogesh'])
    print("Akash's favourite number:",friends['Akash'])

    print("\n")


if __name__ == '__main__':
    exercise_6_2()

