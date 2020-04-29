# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    tri = []
    r = []
    for x in range(n):
        l = len(r)
        r = [1 if i==0 or i==l else r[i-1]+r[i] for i in range(l+1)]
        tri.append(r)
    return tri

def triangle(n):
    return [d.setdefault(j, [sum(d[len(d)-1][max(i, 0):i+2]) for i in range(-1, j)])
        for j, d in enumerate([{0: [1]}] * n)]

def triangle(n):
    ans = []
    row = [1]
    for _ in range(n):
        ans.append(row)
        row = [i+j for i,j in zip([0]+row, row+[0])]
    return ans

def triangle(n):
    def g():
        row = [1]; yield row
        for _ in range(n-1):
            row = [i+j for i,j in zip([0]+row, row+[0])]
            yield row
    return list(g())


#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
