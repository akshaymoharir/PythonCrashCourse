
## Python Crash Course

# Exercise 6.7: People:  
#               Start with the program you wrote for Exercise 6-1 (page 102). 
#               Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
#               Loop through your list of people. As you loop through the list, print everything you know about each person.
#


def exercise_6_7():

    print("\n")
    
    myInfo = {
                'first_name':'Akshay',
                'last_name':'Moharir',
                'age':29,
                'city':'Novi'
            }

    yogeshInfo = {
        'first_name':'Yogesh',
        'last_name':'Dalal',
        'age':29,
        'city':'Novi'
    }

    manasiInfo = {
        'first_name':'Manasi',
        'last_name':'Kshirsagar',
        'age':28,
        'city':'Pune'
    }

    people = [myInfo, yogeshInfo, manasiInfo]

    for person in people:
        print("\nFollowing is information about",person['first_name'])
        print("Name:", person['first_name'] + " " + person['last_name'])
        print("Age:", person['age'])
        print("City:", person['city'])
        print("***********************")

    print("\n")


if __name__ == '__main__':
    exercise_6_7()

