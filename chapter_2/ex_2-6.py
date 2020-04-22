## Python Crash Course

# Exercise 2.6: Famous Quote 2: 
#               Repeat Exercise 2-5, but this time store the famous person's name in a variable called famous_person. 
#               Then compose your message and store it in a new variable called message. Print your message.



def main():
    nameOfScientist = "Albert Einstein"
    connectingSentence = ' said, "'
    quote_1 = 'Compound interest is the 8th wonder of the world. He who understands it, earns it; he who doesn\'t, pays it."'
    
    message = nameOfScientist + connectingSentence + quote_1
    print(message)

if __name__ == '__main__':
    main()

