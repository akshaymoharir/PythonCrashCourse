
## Python Crash Course

# Exercise 6.6: Polling:  
#               Use the code in favorite_languages.py (page 104) .
#               • Make a list of people who should take the favorite languages poll. 
#                   Include some names that are already in the dictionary and some that are not .
#               • Loop through the list of people who should take the poll. 
#                   If they have already taken the poll, print a message thanking them for responding. 
#                   If they have not yet taken the poll, print a message inviting them to take the poll.

def exercise_6_6():

    print("\n")

    print("Following are key-value pairs stored in a dictionary..\n")
    
    #favorite_languages = { 'jen': 'python',
    #                        'sarah': 'c', 
    #                        'edward': 'ruby', 
    #                        'phil': 'python', }

    peopleWhoShouldTakePoll = {'Akshay':'', 
                                'Akash':'', 
                                'Jeremy':'',
                                'Larry':'',
                                'jen':'Python',
                                'sarah':'C',
                                'edward':'Ruby',
                                'phil':'Python',}

    
    for name, language in peopleWhoShouldTakePoll.items():
        if(language!=''):
            print("Thank you " + name.title() + " for taking poll..! Your favorite language is " + language.title() + ".")
        else:
            print(name.title() + " , Could you please take poll to answer your favourite language..")

    print("\n")


if __name__ == '__main__':
    exercise_6_6()

