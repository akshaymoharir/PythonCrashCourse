
## Python Crash Course

# Exercise 5.4: Alien Colors #2:  
#               Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#                • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#                • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#                • Write one version of this program that runs the if block and another that runs the else block.
#


def exercise_5_4():

    print("\n")

    alien_color = 'green'
    if(alien_color=='green'):
        print("You killed",alien_color,"alien. You earned 5 points")
    else:
        print("You killed",alien_color,"alien. You earned 10 points")
    print("\n")


    alien_color = 'yellow'
    if(alien_color=='green'):
        print("You killed",alien_color,"alien. You earned 5 points")
    else:
        print("You killed",alien_color,"alien. You earned 10 points")
    print("\n")

if __name__ == '__main__':
    exercise_5_4()

