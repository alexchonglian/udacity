# -----------------
# User Instructions
# 
# This problem deals with the one-player game foxes_and_hens. This 
# game is played with a deck of cards in which each card is labelled
# as a hen 'H', or a fox 'F'. 
# 
# A player will flip over a random card. If that card is a hen, it is
# added to the yard. If it is a fox, all of the hens currently in the
# yard are removed.
#
# Before drawing a card, the player has the choice of two actions, 
# 'gather' or 'wait'. If the player gathers, she collects all the hens
# in the yard and adds them to her score. The drawn card is discarded.
# If the player waits, she sees the next card. 
#
# Your job is to define two functions. The first is do(action, state), 
# where action is either 'gather' or 'wait' and state is a tuple of 
# (score, yard, cards). This function should return a new state with 
# one less card and the yard and score properly updated.
#
# The second function you define, strategy(state), should return an 
# action based on the state. This strategy should average at least 
# 1.5 more points than the take5 strategy.

import random
from functools import update_wrapper

def foxes_and_hens(strategy, foxes=7, hens=45):
    """Play the game of foxes and hens."""
    # A state is a tuple of (score-so-far, number-of-hens-in-yard, deck-of-cards)
    state = (score, yard, cards) = (0, 0, 'F'*foxes + 'H'*hens)
    while cards:
        action = strategy(state)
        state = (score, yard, cards) = do(action, state)
    return score + yard

def do(action, state):
    "Apply action to state, returning a new state."
    # Make sure you always use up one card.
    score, yard, cards = state
    foxes = cards.count('F')
    hens  = cards.count('H')
    draw_fox = (random.random() <= (foxes+0.0)/(foxes+hens))
    if action == 'wait':
        if draw_fox:
            return (score, 0, 'F'*(foxes-1)+'H'*hens)
        else:
            return (score, yard+1, 'F'*foxes+'H'*(hens-1))  
    elif action == 'gather':
        if draw_fox:
            return (score+yard, 0, 'F'*(foxes-1)+'H'*hens)
        else:
            return (score+yard, 0, 'F'*foxes+'H'*(hens-1))

def take5(state):
    "A strategy that waits until there are 5 hens in yard, then gathers."
    (score, yard, cards) = state
    if yard < 5:
        return 'wait'
    else:
        return 'gather'

def take3(state):
    (score, yard, cards) = state
    if yard < 3:
        return 'wait'
    else:
        return 'gather'

def average_score(strategy, N=1000):
    return sum(foxes_and_hens(strategy) for _ in range(N)) / float(N)

def superior(A, B=take5):
    "Does strategy A have a higher average score than B, by more than 1.5 point?"
    return average_score(A) - average_score(B) > 1.5
"""
def strategy(state):
    (score, yard, cards) = state
    foxes = cards.count('F')
    hens  = cards.count('H')
    if (foxes+0.0)/(foxes+hens) > 0.37:
        return 'gather'
    else:
        return take5(state)
"""

def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f

@memo
def best_score(state):
    (yard, cards) = state

    foxes = cards.count('F')
    hens = cards.count('H')

    if foxes == 0:
        return yard + hens, 'wait'
    if hens == 0:
        return yard, 'gather'

    prob_of_fox = (foxes+0.0) / (hens + foxes)

    cards_less_1_hen = cards.replace('H', "", 1)
    cards_less_1_fox = cards.replace('F', "", 1)

    gather_score = (prob_of_fox * best_score((0, cards_less_1_fox))[0]) + ( (1-prob_of_fox) * best_score((0, cards_less_1_hen))[0] )
    gather_score += yard

    wait_score = (prob_of_fox * best_score((0, cards_less_1_fox))[0]) + ( (1-prob_of_fox) * best_score((yard+1, cards_less_1_hen))[0] )

    if gather_score > wait_score:
        return gather_score, 'gather'
    return wait_score, 'wait'

def strategy_best(state):
    score, strat = best_score((state[1], state[2]))
    return strat

def strategy_norvig(state):
    (score, yard, cards) = state
    if 'F' not in cards:
        return 'wait'
    elif yard >= 3:
        return 'gather'
    else:
        return 'wait'

def test():
    gather = do('gather', (4, 5, 'F'*4 + 'H'*10))
    assert (gather == (9, 0, 'F'*3 + 'H'*10) or 
            gather == (9, 0, 'F'*4 + 'H'*9))
    
    wait = do('wait', (10, 3, 'FFHH'))
    assert (wait == (10, 4, 'FFH') or
            wait == (10, 0, 'FHH'))
    
    a1= average_score(take5)
    a2= average_score(take3)
    print a1, a2, a2-a1
    #assert superior(strategy)
    return 'tests pass'

print test()   


