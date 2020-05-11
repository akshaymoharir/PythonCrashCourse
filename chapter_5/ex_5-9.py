
## Python Crash Course

# Exercise 5.9: No Users:  
#               Add an if test to hello_admin.py to make sure the list of users is not empty.
#               • If the list is empty, print the message We need to find some users!
#               • Remove all of the usernames from your list, and make sure the correct
#                    message is printed.
#

# Following function prints a greeting for user
def GreetUser(username):
    if(username=='admin'):
        print("\nHello admin, Would you like to see access report?")
    elif(username==''):
        print("\nEmpty user name")
    else:
        print("\nHello",username,"thank you for logging in again..!")
    
def exercise_5_8():

    print("\n")
    
    print("\ntest-1")
    users = ['admin','Adam','Beckie','Cayun','Doug','']
    for user in users:
        GreetUser(user)

    print("\ntest-2")
    moreUsers = []
    if(moreUsers):
        for anotherUser in moreUsers:
            GreetUser(anotherUser)
    else:
        print("We need to find more users!")

    print("\n")


if __name__ == '__main__':
    exercise_5_8()

