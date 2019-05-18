# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here:
        return {(hr, tr, time): a for hr, tr, time, a in how_to_move(here, there, t, '->')}
    elif 'light' in there:
        return {(tr, hr, time): a for hr, tr, time, a in how_to_move(there, here, t, '<-')}

def how_to_move(here, there, t, direction):
    here, there = list(here), list(there)
    here.remove('light')
    there.append('light')
    for p in here:
        start, end = here[:], there[:]
        start.remove(p); end.append(p)
        yield frozenset(start), frozenset(end), t+p, (p,p,direction)
    if len(here) <= 1:return
    for p1 in here:
        for p2 in here:
            if p1 != p2:
                start, end = here[:], there[:]
                start.remove(p1); start.remove(p2); end.append(p1); end.append(p2)
                yield frozenset(start), frozenset(end), t+max(p1,p2), (p1,p2,direction)

def how_to_move2(here, there, t, direction):
    here, there = list(here), list(there)
    here.remove('light')
    there.append('light')
    for p1 in here:
        for p2 in here:
            start, end = here[:], there[:]
            start.remove(p1); end.append(p1); 
            if p1 != p2:
                start.remove(p2); end.append(p2);
            yield frozenset(start), frozenset(end), t+max(p1,p2), (p1,p2,direction)

def test():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()