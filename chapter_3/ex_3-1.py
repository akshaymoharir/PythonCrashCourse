
## Python Crash Course

# Exercise 3.1: Names: 
#               Store the names of a few of your friends in a list called names. 
#               Print each person's name by accessing each element in the list, one at a time..

def main():
    names = ['Alice', 'Brad', 'Charlie', 'Doug', 'Evan', 'Frank', 'George', 'Henry', 'Ingrid', 'Jeremy']
    print("My friends are: ")
    for i in range(0,len(names)):
        print(names[i].title())

if __name__ == '__main__':
    main()

