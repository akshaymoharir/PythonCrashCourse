
## Python Crash Course

# Exercise 5.8: Hello Admin:  
#               Make a list of five or more usernames, including the name 'admin'. 
#               Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#               Loop through the list, and print a greeting to each user:
#                   • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#                   • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
#

# Following function calucales score for a given alien color. Returns the score.
def GreetUser(username):
    if(username=='admin'):
        print("\nHello admin, Would you like to see access report?")
    else:
        print("\nHello",username,"thank you for logging in again..!")
        

def exercise_5_8():

    print("\n")
    
    print("\ntest-1")
    users = ['admin','Adam','Beckie','Cayun','Doug']
    for user in users:
        GreetUser(user)

    print("\n")


if __name__ == '__main__':
    exercise_5_8()

