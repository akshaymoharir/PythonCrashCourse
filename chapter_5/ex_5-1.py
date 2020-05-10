
## Python Crash Course

# Exercise 5.1: Conditional Tests:  
#               Write a series of conditional tests. 
#               Print a statement describing each test and your prediction for the results of each test. 
#               Your code should look something like this:
#                car = 'subaru'
#                print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
#                print("\nIs car == 'audi'? I predict False.") print(car == 'audi')
#                • Look closely at your results, and make sure you understand why each line evaluates to True or False.
#                • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
#


def exercise_5_1():

    print("\n")

    # test-1
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.") 
    print(car == 'subaru')
    
    #test-2
    print("\nIs car == 'audi'? I predict False.") 
    print(car == 'audi',"\n")
    
    #test-3
    print("If car != 'audi', I predict True")
    print(car != 'audi',"\n")

    # test-4
    print("If car != 'subaru', I expect False")
    print(car!='subaru',"\n")

if __name__ == '__main__':
    exercise_5_1()

