# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    delta = [(2,0,1), (1,1,1), (0,2,1), (1,0,1), (0,1,1)]
    if B1 == 1:
        for d in delta:
            for i,d in zip((M1, C1, B1), delta):
                print i,d
    elif B2 == 1:
        pass
        #s = [(i+d, j-d) for i,j,d in zip((M1, C1, B1), (M2, C2, B2), delta)]
        #print s

def csuccessors(state):
    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        items += [(sub(state,delta), a+'->') for delta, a in deltas.items()]
    elif B2 > 0:
        items += [(add(state,delta), '<-'+a) for delta, a in deltas.items()]
    return dict(items)


deltas = {
    (2,0,1,-2, 0,-1): 'MM',
    (0,2,1, 0,-2,-1): 'CC',
    (1,1,1,-1,-1,-1): 'MC',
    (1,0,1,-1, 0,-1): 'M',
    (0,1,1, 0,-1,-1): 'C',
}

def add(x,y):
    return tuple(i+j for i,j in zip(x,y))
def sub(x,y):
    return tuple(i-j for i,j in zip(x,y))

def test():
    print csuccessors((2, 2, 1, 0, 0, 0))
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    print csuccessors((1, 1, 0, 4, 3, 1))
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()