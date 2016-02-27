# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 01:29:31 2016

@author: moh
"""
#extracts a collection of birth dates from the user and determine if 
# each individual is at least 21 years old
from date import Date

def main():
    # Date before which the person must have been born to be 21 or older
    bornBefore =  Date(6, 1 , 1998)
    
    # Extract birth dates from the user and determine if 21 or older
    date = promptAndExtractDate()
    while date is not None :
        if date <= bornBefore :
            print ("Is at least 21 years of age: ", date)
        date = promptAndExtractDate()

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
    
#call the main routine
main()
