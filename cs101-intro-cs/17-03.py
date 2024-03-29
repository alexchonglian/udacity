# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(secs):
    mins = int(secs // 60)
    secs = secs % 60
    hours = int(mins // 60)
    mins = mins % 60
    ret = [str(hours), None, str(mins), None, str(secs), None]
    if hours > 1 or hours == 0: ret[1] = ' hours, '
    else: ret[1] = ' hour, '
    if mins > 1 or mins == 0: ret[3] = ' minutes, '
    else: ret[3] = ' minute, '
    if secs > 1 or secs == 0: ret[5] = ' seconds'
    else: ret[5] = ' second'
    return ''.join(ret)
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds