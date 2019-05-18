from fractions import Fraction
from itertools import product as prod

sex = 'BG'
day = '1234567'
def product(*vars):
    return map(''.join, prod(*vars))

two_kids = product(sex, sex)

one_boy = [s for s in two_kids if 'B' in s]

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

print condP(two_boys, one_boy)

two_kids_bday = product(sex, day, sex, day)
boy_tuesday = [s for s in two_kids_bday if 'B2' in s]

print condP(two_boys, boy_tuesday)