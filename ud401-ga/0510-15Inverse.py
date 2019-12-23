"""
Definition: x is the multiplicative inverse of z mod N
    if xz ≡ 1 mod N

Notation:   x ≡ z^-1 mod N
            z ≡ x^-1 mod N

Example inverse of N = 14
1 => 1
2 => None
3 => 5
4 => None
5 => 3
6 
7
8
9 => 11
13 => 13

when does the inverse exist?

Theorem: x^-1 mod N exists iff gcd(x,N) == 1, no common divisor

prove by contradiction, inverse, if exist, is unque


"""