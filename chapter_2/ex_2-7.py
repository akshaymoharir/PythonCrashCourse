
## Python Crash Course

# Exercise 2.7: Stripping Names: 
#               Store a person's name, and include some whitespace characters at the beginning and end of the name. 
#               Make sure you use each character combination, "\t" and "\n", at least once.
#               Print the name once, so the whitespace around the name is displayed.
#               Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


def main():
    nameOfPerson = "  Akshay  \t Prabhakar \n   Moharir  \t   "
    print("Name of Person: '" + nameOfPerson + "'")
    print("Name of Person lstrip(): '" + nameOfPerson.lstrip() + "'")
    print("Name of Person rstrip(): '" + nameOfPerson.rstrip() + "'")
    print("Name of Person strip(): '" + nameOfPerson.strip() + "'")



if __name__ == '__main__':
    main()