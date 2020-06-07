
## Python Crash Course

# Exercise 8.6: City Names:  
#               Write a function called city_country() that takes in the name of a city and its country.
#               The function should return a string formatted like this: "Santiago, Chile"
#               Call your function with at least three city-country pairs, and print the value that’s returned.
#

def city_country(city='',country=''):

    print("\n")
    print('"',city,",",country,'"')
    


if __name__ == '__main__':

    city_country(city='Reykjavik',country="Sweeden")
    city_country(city="Santiago",country="Chille")
    city_country(city="Sydney",country="Australia")


