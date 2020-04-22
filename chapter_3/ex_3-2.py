
## Python Crash Course

# Exercise 3.2: Greetings: 
#               Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#               The text of each message should be the same, but each message should be personalized with the person’s name.

def main():
    names = ['Alice', 'Brad', 'Charlie', 'Doug', 'Evan', 'Frank', 'George', 'Henry', 'Ingrid', 'Jeremy']
    message = ", we studied together at Oakland University for Masters program in Electrical and Computer Engineering."
    for i in range(0,len(names)):
        print("Hello", names[i].title(), message )

if __name__ == '__main__':
    main()

