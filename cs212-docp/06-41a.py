import re

def compile_word(word):
    if not word.isupper():
        return word
    res = []
    i = 1
    for w in reversed(word):
        res.append("%s*%s"%(i, w))
        i*=10
    return '('+'+'.join(res)+')'

def compile_formula(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ','.join(letters)
    print re.split('([A-Z]+)', formula)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    print tokens
    body = ''.join(tokens)
    f = 'lambda %s: %s' %(params, body)
    print f
    return eval(f), letters

compile_formula('YOU==ME**2')