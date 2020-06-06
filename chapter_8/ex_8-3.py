
## Python Crash Course

# Exercise 8.3: T-Shirt:  
#               Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#               The function should print a sentence summarizing the size of the shirt and the message printed on it.
#               Call the function once using positional arguments to make a shirt.
#               Call the function a second time using keyword arguments.
#


def make_shirt(size,message):

    print("\n")
    print("Message on T-shirt:", message)
    print("Size of T-shirt:",size)    
    print("\n")


if __name__ == '__main__':
    make_shirt(message="It's our potential that grounds you!",size=40)


