
## Python Crash Course

# Exercise 3.7: Shrinking Guest List:  
#               You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#               • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#               • Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#                   Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#               • Print a message to each of the two people still on your list, letting them know they’re still invited .
#               • Use del to remove the last two names from your list, so you have an empty list. 
#                   Print your list to make sure you actually have an empty list at the end of your program .


def main():
    
    # Prepare empty list for invitees 
    dinnerInvitees = []

    # Add invitees one by one in the invitees list
    dinnerInvitees.append('Andrew Ng')
    dinnerInvitees.append('Narendra Modi')
    dinnerInvitees.append('Jordon')
    sendInvites(dinnerInvitees)
   
    # Following person cant make it to the dinner party
    personWhoCantMake = dinnerInvitees.pop(1)

    # Print that one of the Guests cant make it to the party
    print(personWhoCantMake,"can't make it to the birthday party!")

    # Following person is the new guest to the party
    anotherGuestToInvite = 'Abdul Kalam'
    print(anotherGuestToInvite,"is coming to the party!!")
    print("Sending second set of invites..")

    # Add new gues to the list
    dinnerInvitees.insert(1, anotherGuestToInvite)
    
    # Send another set of invites
    sendInvites(dinnerInvitees)

    # Insert one guest at the top of the list
    dinnerInvitees.insert(0, 'Aryabhatta')

    # Insert one guest in the middle of the list
    dinnerInvitees.insert(2, 'Ramanujan')

    # Append one guest to the end of the list
    dinnerInvitees.append('ShriKrishna')

    # Send invitations one last time
    sendInvites(dinnerInvitees)

    # Bigger dinner table is not available and only 2 invitees can join
    for i in range(len(dinnerInvitees)):
        if len(dinnerInvitees) > 2:
            nameOfPerson = dinnerInvitees.pop()
            print("Hello", nameOfPerson, ", my apologies for invitation that I sent out, but the dinner table is not available for now."
            " We will go for dinner some other day!")
    # Send invite to only 2 guests that will be joining party
    sendInvites(dinnerInvitees)

    # Delete name of all guests and make the list empty
    for m in range(len(dinnerInvitees)):
        del dinnerInvitees[0]

    # Print list to ensure that list is empty
    print("Following is the list at the end of exercise 3.7:")
    print(dinnerInvitees)


def sendInvites(dinnerInvitees):
    
    # Send invitation to invitees
    for i in range(len(dinnerInvitees)):
        
        # Generic greeting message
        greetingMessage = "Hi " +  str(dinnerInvitees[i]) + ", it's my birthday today, would you join us for the dinner? " \
                            "\nWe also have following guests joining us: "
        
        # Create list of other guests at the dinner                     
        listOfInvitees = dinnerInvitees.copy()
        del listOfInvitees[i]
        
        # Print invitation
        print("\n### \t Birthday Bash \t ###")
        print(greetingMessage)

        # Print list of other guests
        for x in range(len(listOfInvitees)):
            print(listOfInvitees[x])

        # Print end of invitation    
        print("\n###########################\n\n") 


if __name__ == '__main__':
    main()

