"""
for 0≤i≤n, 0≤b≤B:
    K(i,b) = max value
    using subset of object 1..i and total weight ≤ b

Goal: compute K(n,B)
"""

# Knapsack 1: one copy per object
def knapsack1_table(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    K = [[0] * (bagsize+1) for _ in range(n)]
    #no need to init, already zero
    #for i in range(n): K[i][0] = 0
    for b in range(bagsize+1):
        if weights[0] <= b:
            K[0][b] = values[0]
    for i in range(1, n):
        for b in range(1,bagsize+1):
            wi = weights[i]
            if wi <= b:
                K[i][b] = max(values[i]+K[i-1][b-wi], K[i-1][b])
            else:
                K[i][b] = K[i-1][b]
    for row in K:print(row)
    return K[-1][-1]

def knapsack1_row(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    # no need to save entire table, prev row will suffice
    prev = [values[0] if weights[0] <= b else 0 for b in range(bagsize+1)]
    print(prev)
    for i in range(1, n):
        curr = []
        for b in range(bagsize+1):
            wi = weights[i]
            curr.append(max(values[i]+prev[b-wi], prev[b]) if wi <= b else prev[b])
        prev = curr
        print(prev)
    return prev[-1]

def knapsack1_shorter(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    # no need to save entire table, prev row will suffice
    K = [values[0] if weights[0] <= b else 0 for b in range(bagsize+1)]
    print(K)
    for i in range(1, n):
        K = [max(values[i]+K[b-weights[i]], K[b]) if weights[i] <= b else K[b]
            for b in range(bagsize+1)]
        print(K)
    return K[-1]


# Knapsack 2: unlimited supply per object
# video 10-13
def knapsack2_table(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    K = [[0] * (bagsize+1) for _ in range(n)]
    #no need to init, already zero
    #for i in range(n): K[i][0] = 0
    for b in range(bagsize+1):
        if weights[0] <= b:
            K[0][b] = values[0]
    for i in range(1, n):
        for b in range(1,bagsize+1):
            wi = weights[i]
            if wi <= b:
                K[i][b] = max(values[i]+K[i][b-wi], K[i-1][b])
            else:
                K[i][b] = K[i-1][b]
    for row in K:print(row)
    return K[-1][-1]

def knapsack2_row(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    prev = [values[0] if weights[0] <= b else 0 for b in range(bagsize+1)]
    print(prev)
    for i in range(1, n):
        curr = []
        for b in range(bagsize+1):
            wi = weights[i]
            curr.append(max(values[i]+curr[b-wi], prev[b]) if wi <= b else prev[b])
        prev = curr
        print(prev)
    return prev[-1]

# video 13-14
def knapsack2_redesign(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    K = [0]
    for b in range(1,bagsize+1):
        curr = 0
        for wi, vi in zip(weights, values):
            if wi <= b and vi+K[b-wi] > curr:
                curr = vi+K[b-wi]
        K.append(curr)
    print(K)
    return K[-1]

# video 16
def knapsack2_trace(weights, values, bagsize):
    assert len(weights) == len(values)
    n = len(weights)
    K, S = [0], [-1]
    for b in range(1,bagsize+1):
        curr, chosen = 0, -1
        for i, (wi, vi) in enumerate(zip(weights, values)):
            if wi <= b and vi+K[b-wi] > curr:
                curr = vi+K[b-wi]
                chosen = i
        K.append(curr)
        S.append(chosen)
    #print(K, S)
    path = []
    n = len(S)-1
    idx = S[n]
    while idx >= 0:
        w = weights[idx]
        v = values[idx]
        path.append((w,v))
        n -= w
        idx = S[n]
    print(path)
    return K[-1]

ks = knapsack2_trace

def test1():
    W = [5, 4, 3, 2]
    V = [5, 3, 3, 2]
    B = 7
    ks(W, V, B)

def test2():
    W = [15, 12, 10, 5]
    V = [15, 10,  8, 1]
    B = 22
    ks(W, V, B)

def test3():
    W = [5, 4, 3, 2]
    V = [5, 3, 4, 3]
    B = 6
    ks(W, V, B)

if __name__ == '__main__':
    test1()
    test2()
    test3()