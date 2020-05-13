
## Python Crash Course

# Exercise 6.4: Glossary#2:  
#               Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) 
#                   by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. 
#               When you’re sure that your loop works, add five more Python terms to your glossary. 
#               When you run your program again, these new words and meanings should automatically be included in the output.
#


def exercise_6_4():

    print("\n")

    print("Following are key-value pairs stored in a dictionary..\n")
    
    pythonChapters = {
                'HelloWorld':"Introduction to Python. First program.",
                'Lists':"Collection of items in particular order.",
                'Variables':"Different kind of data we can work with.",
                'Dictionary':"Limitless type to store information.",
                'Games In Python':"I am excited to develop my own game using Python!"
            }

    for chapter in pythonChapters.keys():
        print(chapter.title(), ":", pythonChapters[chapter]);

    print("\n")


if __name__ == '__main__':
    exercise_6_4()

