
## Python Crash Course

# Exercise 5.5: Alien Colors #3:  
#               Turn your if-else chain from Exercise 5-4 into an if-elif- else chain.
#               • If the alien is green, print a message that the player earned 5 points.
#               • If the alien is yellow, print a message that the player earned 10 points.
#               • If the alien is red, print a message that the player earned 15 points.
#               • Write three versions of this program, making sure each message is printed for the appropriate color alien.
#

# Following function calucales score for a given alien color. Returns the score.
def CalculateScore(alien_color):
    score = 0
    if(alien_color=='green'):
        score = 5
    elif(alien_color=='yellow'):
        score = 10
    else:
        score = 15
    
    return score


def exercise_5_5():

    print("\n")
    
    print("\ntest-1")
    alien_color = 'green'
    score = 0
    score = CalculateScore(alien_color)
    print("You killed",alien_color,"alien. You earned", score, "points.")

    print("\ntest-2")
    alien_color = 'red'
    score = 0
    score = CalculateScore(alien_color)
    print("You killed",alien_color,"alien. You earned", score, "points.")

    print("\ntest-3")
    alien_color = 'yellow'
    score = 0
    score = CalculateScore(alien_color)
    print("You killed",alien_color,"alien. You earned", score, "points.")

    print("\n")


if __name__ == '__main__':
    exercise_5_5()

