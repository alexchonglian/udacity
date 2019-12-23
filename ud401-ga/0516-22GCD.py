def euclid(x,y):
    # input: integers x,y where x≥y≥0
    # output: gcd(x,y)
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    else:
        return euclid(y, x%y)

def extended_euclid0(x,y):
    # input: integers x,y where x≥y≥0
    # output: integer d, alpha, beta
    # where d = gcd(x,y) & d = x*alpha + y*beta
    if x < y:
        x,y = y,x
    if y == 0:
        return x, 1, 0
    else:
        d, alpha, beta = extended_euclid0(y, x%y)
        return d, beta, alpha-(x//y)*beta

def extended_euclid1(x,y):
    # using divmod
    # input: integers x,y where x≥y≥0
    # output: integer d, alpha, beta
    # where d = gcd(x,y) & d = x*alpha + y*beta
    if x < y:
        x,y = y,x
    if y == 0:
        return x, 1, 0
    else:
        div, rem = divmod(x, y)
        d, alpha, beta = extended_euclid1(y, rem)
        return d, beta, alpha-div*beta


if __name__ == '__main__':
    print(euclid(48, 28))
    print(euclid(125, 37))
    print(euclid(360, 7))
    print(extended_euclid1(48, 28))
    print(extended_euclid1(125, 37))
    print(extended_euclid1(360, 7))