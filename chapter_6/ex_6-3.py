
## Python Crash Course

# Exercise 6.3: Glossary:  
#               A Python dictionary can be used to model an actual dictionary. 
#               However, to avoid confusion, let’s call it a glossary.
#                • Think of five programming words you’ve learned about in the previous chapters. 
#                    Use these words as the keys in your glossary, and store their meanings as values .
#                • Print each word and its meaning as neatly formatted output. 
#                    You might print the word followed by a colon and then its meaning, or 
#                    print the word on one line and then print its meaning indented on a second line. 
#                Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
#


def exercise_6_3():

    print("\n")
    
    pythonChapters = {
                'HelloWorld':"Introduction to Python. First program.",
                'Lists':"Collection of items in particular order.",
                'Variables':"Different kind of data we can work with.",
                'Dictionary':"Limitless type to store information."
            }

    print("Hello World:\n",pythonChapters['HelloWorld'])
    print("\nLists in Python:\n",pythonChapters['Lists'])
    print("\nVariables:\n",pythonChapters['Variables'])
    print("\nDictionary:\n",pythonChapters['Dictionary'])

    print("\n")


if __name__ == '__main__':
    exercise_6_3()

