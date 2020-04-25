
## Python Crash Course

# Exercise 3.6: More Guests:  
#               You just found a bigger dinner table, so now more space is available . Think of three more guests to invite to dinner.
#               • Start with your program from Exercise 3-4 or Exercise 3-5. 
#                   Add a print statement to the end of your program informing people that you found a bigger dinner table.
#               • Use insert() to add one new guest to the beginning of your list.
#               • Use insert() to add one new guest to the middle of your list.
#               • Use append() to add one new guest to the end of your list.
#               • Print a new set of invitation messages, one for each person in your list.


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

