
## Python Crash Course

# Exercise 3.5: Changing Guest List:  
#               You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#               You’ll have to think of someone else to invite.
#               • Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.
#               • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#               • Print a second set of invitation messages, one for each person who is still in your list.

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

    # Add new gues to the list
    dinnerInvitees.insert(1, anotherGuestToInvite)
    
    # Send another set of invites
    sendInvites(dinnerInvitees)

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

