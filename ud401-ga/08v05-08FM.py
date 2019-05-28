from time import time

def fm(x,y):
    return x*y

def fm0(x, y, n):
    # input: n-bit integers x & y, n = 2^k
    # output: z = x*y
    #print("fm0(%s, %s, %s)"%(bin(x), bin(y), n))
    if n <= 1: return x*y
    hf = n//2
    mask = (1 << hf) - 1
    xl,xr,yl,yr = x>>hf, x&mask, y>>hf, y&mask
    a,b,c,d = fm0(xl,yl,hf), fm0(xr,yr,hf), fm0(xl,yr,hf), fm0(xr,yl,hf)
    z = (1<<n)*a + (1<<hf)*(c+d) + b
    return z

def fm1(x, y):
    # input: n-bit integers x & y, n = 2^k
    # output: z = x*y
    #print("fm1(%s, %s)"%(bin(x), bin(y)))
    xlen, ylen = x.bit_length(), y.bit_length()
    n = max(xlen,ylen)
    n = 1 << n.bit_length()
    return fm0(x,y,n)

def fm2(x,y,count=0):
    # input: x (m-bit int), y (n-bit int)
    # output: z = x*y
    # compute bit length for left half and right half?
    # enable full debug?
    def log(msg):
        return
        print(" "*2*count+msg)
    log("fm2(%d=%s, %d=%s)"%(x, bin(x)[2:], y, bin(y)[2:]))
    xlen, ylen = x.bit_length(), y.bit_length()
    log("len: %s %s"%(xlen, ylen))
    n = max(xlen,ylen)
    if min(xlen,ylen) <= 1:
        log("=> %d" % x*y)
        return x*y
    shift = n//2
    log("n, %s, shift: %s" % (n,shift))
    mask = (1 << shift) - 1
    log("mask %s" % mask)
    xl,xr,yl,yr = x>>shift, x&mask, y>>shift, y&mask
    log("xl,xr,yl,yr: %s %s %s %s"%(xl,xr,yl,yr))
    a,b,c,d = fm2(xl,yl,count+1), fm2(xr,yr,count+1), fm2(xl,yr,count+1), fm2(xr,yl,count+1)
    log("a,b,c,d: %s %s %s %s"%(a,b,c,d))
    z = (1<<shift*2)*a + (1<<shift)*(c+d) + b
    log("z=%s"%z)
    return z


def fm3(x,y,count=0):
    # input: x (m-bit int), y (n-bit int)
    # output: z = x*y
    # time: T(n) = 4T(n/2) + O(n)
    xlen, ylen = x.bit_length(), y.bit_length()
    n = max(xlen,ylen)
    if min(xlen,ylen) <= 1:
        return x*y
    shift = n//2
    mask = (1 << shift) - 1
    xl,xr,yl,yr = x>>shift, x&mask, y>>shift, y&mask
    a,b,c,d = fm3(xl,yl,count+1), fm3(xr,yr,count+1), fm3(xl,yr,count+1), fm3(xr,yl,count+1)
    z = (1<<shift*2)*a + (1<<shift)*(c+d) + b
    return z

def fm4(x,y,count=0):
    # Improved Fast Multiplication
    # input: x (m-bit int), y (n-bit int)
    # output: z = x*y
    # time: T(n) = 3T(n/2) + O(n)
    xlen, ylen = x.bit_length(), y.bit_length()
    n = max(xlen,ylen)
    if min(xlen,ylen) <= 1:
        return x*y
    shift = n//2
    mask = (1 << shift) - 1
    xl,xr,yl,yr = x>>shift, x&mask, y>>shift, y&mask
    a,b,c = fm4(xl,yl,count+1), fm4(xr,yr,count+1), fm4(xl+xr,yl+yr,count+1)
    z = (1<<shift*2)*a + (1<<shift)*(c-a-b) + b
    return z

# not taught in ud401 but
# it reminds me of another way to multiply
def mul0(x, y):
    z = 0
    while y > 0:
        z = z + x
        y = y - 1
    return z

def mul1(x, y):
    z = 0
    while y > 0:
        if y % 2 == 1: z = z + x
        x = x << 1
        y = y >> 1
    return z 

def run_tests(name):
    f = globals().get(name)
    assert f(50, 3) == 150
    assert f(12, 3) == 36
    assert f(10, 3) == 30
    assert f(4, 5) == 20
    assert f(20, 5) == 100
    assert f(17, 5) == 85
    assert f(9, 3) == 27
    assert f(1000, 10) == 10000

def timed_exec(name):
    f = globals().get(name)
    start = time()
    for i in range(100):
        f(29642949672949672964, 29496729642964294967)
    end = time()
    print("%s takes %f" % (name, end-start))

if __name__ == '__main__':
    # this is so stupid
    timed_exec('fm') # fm takes 0.000021
    timed_exec('fm3') # fm3 takes 0.228150
    timed_exec('fm4') # fm4 takes 0.153585

    #print(2964294967*2949672964)
    #print(fm0(2964294967, 2949672964, 32))
    #print(fm1(2964294967, 2949672964))
    #print(fm1(1000, 10))
    #print(fm2(2964294967, 2949672964))
    #print(fm2(1000, 10))
    #print(mul0(2964294967, 2949672964)) # wont finish
    #print(mul1(2964294967, 2949672964))
