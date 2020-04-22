## Python Crash Course

# Exercise 2.5: Famous Quote: 
#               Find a quote from a famous person you admire. Print the
#               quote and the name of its author. Your output should look something like the
#               following, including the quotation marks:
#               Albert Einstein once said, A person who never made a mistake never tried anything new.



def main():
    nameOfScientist = "Albert Einstein"
    connectingSentence = ' said, "'
    quote_1 = 'Compound interest is the 8th wonder of the world. He who understands it, earns it; he who doesn\'t, pays it."'
    
    print(nameOfScientist + connectingSentence + quote_1)

if __name__ == '__main__':
    main()

