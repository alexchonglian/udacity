def readable_timedelta(days):
    # insert your docstring here
    """convert days to weeks and days in readable format"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)