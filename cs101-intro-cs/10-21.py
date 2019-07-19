###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    day = day + 1
    month = month + day / 30
    day = day % 30
    year = year + (month-1) / 12
    month = (month-1) % 12 + 1
    return (year, month, day)

print nextDay(2012, 1, 1)
print nextDay(2012, 4, 30)
print nextDay(2012, 12, 1)
print nextDay(1999, 12, 30)
print nextDay(2012, 12, 30)