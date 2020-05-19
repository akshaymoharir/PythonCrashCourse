
## Python Crash Course

# Exercise 6.8: Pets:  
#               Make several dictionaries, where the name of each dictionary is the name of a pet. 
#               In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
#               Next, loop through your list and as you do print everything you know about each pet.
#


def exercise_6_8():

    print("\n")
    
    Shaggy = {
            'kind':'dog',
            'owner':'Akshay',
            }

    Tom = {
            'kind':'cat',
            'owner':'Yogesh',
            }

    Gustav = {
            'kind':'rabbit',
            'owner':'Manasi',
            }

    Jerry = {
            'kind':'mouse',
            'owner':'Akash',
            }

    pets = [Shaggy, Tom, Gustav, Jerry]

    for pet in pets:
        print("\nFollowing is information about pet.")
        print("Kind:", pet['kind'])
        print("Owner:", pet['owner'])
        print("***********************")

    print("\n")


if __name__ == '__main__':
    exercise_6_8()

