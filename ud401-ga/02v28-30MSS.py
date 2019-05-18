"""
practice

[Dasgupta, Papadimitriou, Vazirani]

6.1 contiguous subseq (substring)

6.2 hotel stops

6.3 Yuckdonalds

6.4 string of words

6.11 longest common substring

Approach

1. define subproblem in words
    prefix?
    constraint? (include last element?)

2. recurrence
    T(i) in terms of T(1),...,T(i-1)

6.1

Input a1,...,an

Goal: max sum substring

Subproblem: 
for i in (0..n):
    S(i) = max sum from substring of a1,...,ai, which includes ai

"""

def mss(a):
    dp = [0]
    for ai in a:
        dp.append(ai+max(0,dp[-1]))
    print(dp)
    return max(dp)

if __name__ == '__main__':
    print(mss([-1, 1, -7, 3, 4, 5, -1, -2, 4, -5]))


