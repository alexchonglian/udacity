def knapsack(w, v, B):
    n = len(w)
    assert n == len(v)
    K = [[0]*(B+1) for _ in range(n)]
    for b in range(B+1):
        if w[0] <= b:
            K[0][b] = v[0]
    for i in range(1, n):
        for b in range(1, B+1):
            wi = w[i]
            if wi <= b:
                K[i][b] = max(v[i]+K[i-1][b-wi], K[i-1][b])
            else:
                K[i][b] = K[i-1][b]
        for row in K:print(row)
        print()
    return K[-1][-1]


ks = knapsack

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
    #test2()
    #test3()