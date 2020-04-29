"""
Fibonacci

1st step: define subproblem in words
    F[i] := ith finonacci number

2nd step: state recursive relationship
    F[i] = F[i-1] + F[i-2]

LIS

1st step: define subproblem in words
    L[i] := length of LIS in a1,...,ai which includes ai

2nd step: state recursive relationship
    L[i] = 1+max(L[j] for j<i and a[j] < a[i])


longest increasing subseq
substring == set of consecutive elements (start, end)
subsequence == subset of elements in order
    string you can obtain by deleting elements
"""

def lis0(A):
    # double loop
    size = len(A)
    L = [1]*size
    for i in range(1, size):
        for j in range(i):
            if A[j] < A[i] and L[i] < 1 + L[j]:
                L[i] = 1 + L[j]
    return L

def lis1(A):
    # double loop
    size = len(A)
    dp_val = [1]*size
    dp_loc = [-1]*size
    for i in range(1, size):
        for j in range(i):
            # there may be multiple optimal
            if A[j] < A[i] and dp_val[i] < 1 + dp_val[j]:
                dp_val[i] = 1 + dp_val[j]
                dp_loc[i] = j
    # backtrack
    l = dp_val.index(max(dp_val))
    path = []
    while l != -1:
        path.append(l)
        l = dp_loc[l]
    path.reverse()
    opt = [A[i] for i in path]
    #return path
    return opt

def lis2(A):
    # use max([], default=0)
    # wrong
    size = len(A)
    L = [1]
    for i in range(1, size):
        ai = A[i]
        Li = 1 + max([aj for aj in L if aj < ai], default=0)
        L.append(Li)
    return L

def lis3(a):
    # use max([], default=0)
    size = len(a)
    L = [1]
    for i in range(1, size):
        ai = a[i]
        Li = 1 + max([Lj for Lj, aj in zip(L, a[:i]) if aj < ai], default=0)
        L.append(Li)
    return L

def lis4(a):
    # use max([], default=0)
    size = len(a)
    L = [1]
    for i in range(1, size):
        Li = 1 + max((L[j] for j in range(i) if a[j] < a[i]), default=0)
        L.append(Li)
    return L

if __name__ == '__main__':
    L = lis4([5,7,4,-3,9,1,10,4,5,8,9,3])
    print(L)
    # optimal = [-3,1,4,5,8,9] ?
    # L = [1,2,1,1,3,2,4,3,4,5,6,3]