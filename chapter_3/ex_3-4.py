
## Python Crash Course

# Exercise 3.4: Guest List:  
#               If you could invite anyone, living or deceased, to dinner, who would you invite? 
#               Make a list that includes at least three people you’d like to invite to dinner . 
#               Then use your list to print a message to each person, inviting them to dinner .

def main():
    
    # Prepare empty list for invitees 
    dinnerInvitees = []

    # Add invitees one by one in the invitees list
    dinnerInvitees.append('Andrew Ng')
    dinnerInvitees.append('Narendra Modi')
    dinnerInvitees.append('Jordon')
   
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

