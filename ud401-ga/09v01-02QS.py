"""
Given unsorted list A = [a1,...,an], find the median of A
ceil(n/2) th smallest

Given unsorted list A, find the kth smallest of A

Easy algo: sort A and return kth element

D&C QuickSort style

QuickSort(A):
    1. choose pivot p
    2. partition A into A<p, A=p, A>p
    3. Recursively sort A<p, A>p

"""

from random import shuffle

def qs(A):
    _qs(A, 0, len(A)-1)
    return A

def _qs(A, lo, hi):
    if lo < hi:
        p = partition2(A, lo, hi)
        _qs(A, lo, p-1)
        _qs(A, p+1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] < pivot:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

def partition2(A, lo, hi):
    pivot = A[hi]
    i,j = lo, hi-1
    while True:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i>j:
            break
        else:
            A[i],A[j]= A[j],A[i]
    A[i],A[hi]=A[hi],A[i]
    return i

if __name__ == '__main__':
    print(qs([5,2,20,17,11,13,8,9,11]))
    print(qs([5,2,9,8,11,11,17,20,13]))
    print(qs([54,26,93,17,77,31,44,55,20]))
    print(qs([17,20,93,54,77,31,44,55,26]))
    for i in range(100):
        nums = [5,2,9,8,11,11,17,20,13]
        shuffle(nums)
        assert qs(nums) == [2,5,8,9,11,11,13,17,20]
    for i in range(100):
        nums = [54,26,93,17,77,31,44,55,20]
        shuffle(nums)
        assert qs(nums) == [17,20,26,31,44,54,55,77,93]