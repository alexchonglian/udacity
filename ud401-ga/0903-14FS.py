"""

QuickSort(A):
    1. choose pivot p
    2. partition A into A<p, A=p, A>p
    3. Recursively sort A<p, A>p

QuickSelect(A):
    1. choose pivot p
    2. partition A into A<p, A=p, A>p
    3.
        if k ≤ len(A<p):
            select(A<p, k)
        elif len(A<p) < k ≤ len(A<p)+len(A=p):
            return p
        else:
            select(A>p, k-len(A<p)-len(A=p))

T(n) = T(n/2) + O(n)
thus T(n) = O(n)

Linear Time Media

FastSelect(A):
    input: unsorted A and integer k where 1≤k≤n
    output: kth smallest element in A
    1. break A into n/5 groups G1, G2, ... , Gn/5
    2. for i in 1..n/5: sort Gi and mi = median(Gi)
    3. let S = {m1, m2, ... mn/5}
    4. p = QuickSelect(S, n/10)
    5. partition A into A<p, A=p, A>p
    6. 
        if k ≤ len(A<p):
            select(A<p, k)
        elif len(A<p) < k ≤ len(A<p)+len(A=p):
            return p
        else:
            select(A>p, k-len(A<p)-len(A=p))

"""