#https://rosettacode.org/wiki/Fast_Fourier_transform
#Python:_Recursive
from cmath import exp, pi
 
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k]+T[k] for k in range(N//2)] + \
           [even[k]-T[k] for k in range(N//2)]

if __name__ == '__main__':
    A = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    B = [0, 0.924, 0.707,-0.383,-1,-0.383, 0.707, 0.924, 
        0,-0.924,-0.707, 0.383, 1, 0.383,-0.707,-0.924]
    print(' '.join("%5.3f" % abs(f) for f in fft(A)) )
    print(' '.join("%5.3f" % abs(f) for f in fft(B)) )