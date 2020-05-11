
## Python Crash Course

# Exercise 6.1: Person:  
#               Use a dictionary to store information about a person you know. 
#               Store their first name, last name, age, and the city in which they live. 
#               You should have keys such as first_name, last_name, age, and city. 
#               Print each piece of information stored in your dictionary.
#


def exercise_6_1():

    print("\n")
    
    myInfo = {
                'first_name':'Akshay',
                'last_name':'Moharir',
                'age':29,
                'city':'Novi'
            }

    print("Name:", myInfo['first_name'] + " " + myInfo['last_name'])
    print("Age:", myInfo['age'])
    print("City:", myInfo['city'])

    print("\n")


if __name__ == '__main__':
    exercise_6_1()

