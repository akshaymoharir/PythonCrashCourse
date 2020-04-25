
## Python Crash Course

# Exercise 3.8: Seeing the World:  
#               Think of at least five places in the world you’d like to visit .
#               • Store the locations in a list . Make sure the list is not in alphabetical order.
#               • Print your list in its original order . Don’t worry about printing the list neatly, just print it as a raw Python list.
#               • Use sorted() to print your list in alphabetical order without modifying the actual list.
#               • Show that your list is still in its original order by printing it.
#               • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#               • Show that your list is still in its original order by printing it again.
#               • Use reverse() to change the order of your list . Print the list to show that its order has changed.
#               • Use reverse() to change the order of your list again . Print the list to show it’s back to its original order.
#               • Use sort() to change your list so it’s stored in alphabetical order . Print the list to show that its order has been changed.
#               • Use sort() to change your list so it’s stored in reverse alphabetical order . Print the list to show that its order has changed.


def main():

    # Prepare list of places in the world to visit  
   placesToVisit = ['Paris', 'Seychelles', 'Maldives', 'Hawai', 'Yosemite']

   # Print the raw list
   print("\nI want to visit following places with Manasi in lifetime:")
   print(placesToVisit)

   # Print list in alphabetical order without modifying original list using sorted function
   print("\nPrinting list in alphabetical oreder using 'sorted' function")
   print(sorted(placesToVisit))

   # Print the original list, ensure that sorted function that is used prior did not change the order in original list
   print("\nPrinting original list to ensure that it is intact and in the way as it was defined:")
   print(placesToVisit)
   
   # Print the list in reverse alphabetical order without modifying original list
   print("\nPrinting list in reverse alphabetical order using sorted function:")
   print(sorted(placesToVisit, reverse=True))

   # Print original list to ensure that it is as it was defined in the first place
   print("\nPrinting original list to ensure that it is intact and in the way as it was defined:")
   print(placesToVisit)

   # Use reverse function to reverse the order of the list
   print("\nPrinting the list in reverse order:")
   placesToVisit.reverse()
   print(placesToVisit)

   # Use reverse function again so that list becones back to original as it was defined at the first place
   print("\nReversing the list again to obtain original list:")
   placesToVisit.reverse()
   print(placesToVisit)

   # Sort the original list alphabetically
   print("\nSorting the list alphabetically:")
   placesToVisit.sort()
   print(placesToVisit)

   # Sort the previously sorted list in reverse order
   print("\nReversing the order of places in list that was sorted alphabetically:")
   placesToVisit.sort(reverse=True)
   print(placesToVisit)



if __name__ == '__main__':
    main()

