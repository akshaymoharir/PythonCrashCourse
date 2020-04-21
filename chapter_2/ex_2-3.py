
## Python Crash Course

# Ex 2.3:  Personal Message: Store a persons name in a variable, and print a message to that person. 
# Your message should be simple, such as, Hello Eric, would you like to learn some Python today? 


def main():
    nameOfPerson = "Manasi"
    greet = "Hello " + nameOfPerson
    question_1 = ", Would you like to join me today to learn Python?"
    print(greet + question_1)

if __name__ == '__main__':
    main()

