def fib0(n):
    # recur
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib0(n-1)+fib0(n-2)

def fib1(n):
    # dp
    F = [0,1]
    if n >= 0 and n < 2:
        return F[n]
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]

F = {0:0,1:1}
def fib2(n):
    if n in F:
        return F[n]
    else:
        return fib2(n-1)+fib2(n-2)

def creat_fib():
    cache = {0:0,1:1}
    def f(n):
        if n in cache:
            return cache[n]
        else:
            return f(n-1)+f(n-2)
    # or shorter 
    # def f(n):return cache[n] if n in cache else f(n-1)+f(n-2)
    return f

fib = creat_fib()

if __name__ == '__main__':
    print(fib(0))
    print(fib(5))
    print(fib(10))