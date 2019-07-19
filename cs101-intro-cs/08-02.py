# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days_per_month      = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_per_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_days1 = 0
    num_days2 = 0
    if isLeap(year1): num_days1 = sum(days_per_month_leap[:month1-1]) + day1
    else: num_days1 = sum(days_per_month[:month1-1]) + day1
    if isLeap(year2): num_days2 = sum(days_per_month_leap[:month2-1]) + day2
    else: num_days2 = sum(days_per_month[:month2-1]) + day2
    num_leap_year = 0
    for y in range(year1, year2):
        if isLeap(y): num_leap_year += 1
    num_days_between_years = 365 * (year2-year1) + num_leap_year
    return num_days_between_years + num_days2 - num_days1

def isLeap(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

# Test routine


def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", result
        else:
            print "Test case passed!"

test()
