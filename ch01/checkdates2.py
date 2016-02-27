# pgm: checkdats2.py (modified main() from checkdates.py)
from linearbag import bag
from date import Date

# Prompts for and extracts the Gregorian date components. Returns a Date
# object or None when the user has finished entering dates
def promptAndExtractDate():
    print("Enter a birth date")
    month = int( input("Month (0 to quit): ") )
    if month == 0:
        return None
    else:
        day = int( input("day: "))
        year = int( input("year: "))
        return Date( month, day, year)

def main():
    bornBefore = Date(6, 1, 1988)
    bag = Bag()

    # Extract dates from the user and place them in the bag.
    date = promptAndExtractDate()
    while date is not None :
        bag.add(date)
        date = promptAndExtractDate()

    # Iterate over the bag and check the age.
    for date in bag :
        if date <= bornBefore :
            print("Is at least 21 years of age: ", date)

if __name__ == "__main__":
    main()
