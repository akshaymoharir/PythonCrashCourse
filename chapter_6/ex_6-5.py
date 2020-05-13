
## Python Crash Course

# Exercise 6.5: Rivers:  
#               Make a dictionary containing three major rivers and the country each river runs through. 
#                   One key-value pair might be 'nile': 'egypt'.
#               • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#               • Use a loop to print the name of each river included in the dictionary.
#               • Use a loop to print the name of each country included in the dictionary .

def exercise_6_5():

    print("\n")

    print("Following are key-value pairs stored in a dictionary..\n")
    
    rivers = {
                'Nile':"Egypt",
                'Amazon':"Brazil",
                'Ganges':"India",
                'Narmada':"India",
                'Brahmaputra':"Nepal",
                'Thames':"London"
            }

    for river in rivers.keys():
        print(river.title(), "flows through", rivers[river].title(),".");
    

    print("\n")


if __name__ == '__main__':
    exercise_6_5()

