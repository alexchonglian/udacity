def memo(f):
    cache = {}
    def _f():
        print f(), cache
    return _f

def a():print 'a'
a = memo(a)

def b():print 'b'
b = memo(b)
