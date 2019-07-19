#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
        
        




print fibonacci(36)
#>>> 14930352