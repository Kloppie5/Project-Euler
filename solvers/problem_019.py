
"""
    Monday 0
    Tuesday 1
    Wednesday 2
    Thursday 3
    Friday 4
    Saturday 5
    Sunday 6

    January 31
    February 28/29
    March 31
    April 30
    May 31
    June 30
    July 31
    August 31
    September 30
    October 31
    November 30
    December 31

    For a normal year that starts with 0; we get 0 33614625035 1
    For a leap year that starts with 0; we get 0 34025036146 2
"""

normal_year = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
leap_year =   [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

year_patterns = {}

o = 0
for year in range(1900, 2001) :
    is_leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
    if is_leap_year :
        year_patterns[year] = [(s + o) % 7 for s in leap_year]
        o = (o + 2) % 7
    else :
        year_patterns[year] = [(s + o) % 7 for s in normal_year]
        o = (o + 1) % 7
del year_patterns[1900]

print(sum([1
    for year in year_patterns
    for s in year_patterns[year]
    if s == 6
]))