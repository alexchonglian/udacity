def trace(f):
    level = [0]
    def _f(x):
        level[0] += 1
        print ' '*level[0] + '--> fib(%d)'%x
        res = f(x)
        level[0] -= 1
        return res
    return _f

@trace
def fib(n):
    if n in (0,1):
        return 1
    return fib(n-1)+fib(n-2)

print fib(6)