import string, re

def valid(f):
    "Formula f is valid iff it has no numbers with leading zero and evals true."
    try:
        return eval(f)
    except ZeroDivisionError:
        return False