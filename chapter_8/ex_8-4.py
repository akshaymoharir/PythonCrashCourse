
## Python Crash Course

# Exercise 8.4: Large Shirts:  
#               Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#               Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
#


def make_shirt(size='large',message='I love Python!'):

    print("\n")
    print("Message on T-shirt:", message)
    print("Size of T-shirt:",size)


if __name__ == '__main__':

    # Make a large shirt
    make_shirt()

    # Make a medium shirt
    make_shirt(size='medium')

    # Small shirt 
    make_shirt(size='small',message='Plotly is my favorite plotting tool.')


