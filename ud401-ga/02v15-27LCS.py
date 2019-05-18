"""
input: 2 strings X and Y

goal: find the length of longest string which is a subseq of both X and Y

example:
    __ _  _ 
X = BCDBCDA
     _ ___
Y = ABECBAB

longest = BCBA

step 1:
    design subproblem in words
    try some problem on prefix of input

    for i where 0 ≤ i ≤ n
        let L(i) = length of LCS in X1,...,Xi
                                    Y1,...,Yi
step 2:
    define recurrence
    express L(i) in terms of L(1),...,L(i-1)


L(i,j) := length of LCS in X1,...,Xi and Y1,...,Yj

for x≥1, y≥1:
    L(i,j)  = 1 + L(i-1, j-1) if Xi == Yj
            = max{ L(i-1,j), L(i,j-1)} if Xi ≠ Yj
"""


def lcs1(x, y):
    lenx, leny = len(x)+1, len(y)+1
    L = [[0]*leny for i in range(lenx)]
    for i in range(1,lenx):
        for j in range(1, leny):
            # dp table size is larger than orig seq x and y
            if x[i-1] == y[j-1]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    for row in L:print(row)
    return L[-1][-1]

def lcs2(x, y):
    lenx, leny = len(x), len(y)
    L = [[0]*leny for i in range(lenx)]
    # helper function for border case
    getL = lambda i,j: 0 if i<0 or j<0 else L[i][j]
    for i in range(0, lenx):
        for j in range(0, leny):
            if x[i] == y[j]:
                L[i][j] = 1+getL(i-1,j-1)
            else:
                L[i][j] = max(getL(i,j-1), getL(i-1,j))
    for row in L:print(row)
    return L[-1][-1]

def lcs3(x, y):
    lenx, leny = len(x), len(y)
    L = [[0]*leny for i in range(lenx)]
    # initialize top row and leftmost column
    if x[0] == y[0]: L[0][0] = 1
    for i in range(1, lenx):
        L[i][0] = max(1 if x[i]==y[0] else 0, L[i-1][0])
    for j in range(1, leny):
        L[0][j] = max(1 if y[j]==x[0] else 0, L[0][j-1])
    for i in range(1, lenx):
        for j in range(1, leny):
            if x[i] == y[j]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    for row in L:print(row)
    return L[-1][-1]

def lcs4(x, y):
    lenx, leny = len(x), len(y)
    L = [[0]*leny for i in range(lenx)]
    # another way to initialize top row and leftmost column
    matched = False
    for i in range(0, lenx):
        if x[i]==y[0]: matched = True
        L[i][0] = 1 if matched else 0
    matched = False
    for j in range(0, leny):
        if y[j]==x[0]: matched = True
        L[0][j] = 1 if matched else 0
    for i in range(1, lenx):
        for j in range(1, leny):
            if x[i] == y[j]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    for row in L:print(row)
    return L[-1][-1]

if __name__ == '__main__':
    print(lcs4(list('ABC'), list('BC')))
    print(lcs4(list('BCDBCDA'), list('ABECBAB')))

