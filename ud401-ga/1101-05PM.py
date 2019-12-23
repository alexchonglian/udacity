# polynomial multiplication
# convolution

def pm0(a, b):
    # construct rank one matrix from a & b
    # sum diagonally
    matrix = [[i*j for j in a] for i in b]
    res = [0] * (len(a)+len(b)-1)
    print(res)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[i+j] += matrix[i][j]
    return res

def pm1(a, b):
    res = [0] * (len(a)+len(b)-1)
    for i in range(len(b)):
        for j in range(len(a)):
            res[i+j] += a[j]*b[i]
    return res

if __name__ == '__main__':
    print(pm1([1,2,3], [2,-1,4]))