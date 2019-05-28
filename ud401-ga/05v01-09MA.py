"""
RSA crypto system

Outline:
    Math primer
        modular arithmetics
        inverses
        euclids's GCD algorithms
    Fermat's little theorem
        RSA algo
    Primality testing
        generate random primes

Fact:
    if x ≡ y mod N, and a ≡ b mod N
    then x+a ≡ y+b, xa ≡ yb

321x17 mod 320 = 17
because 321 ≡ 1 mod 320

Modular Exponentiation
7^5 mod 23
7^2 = 49
49 mod 23 = 3
7^4 mod 23 = 3^2 mod 23 = 9
7^5 mod 23 = 7*9 mod 23 = 17

Modular Exponentiation (Fast)
7^25 mod 23
(7^2 mod 23) == (49 mod 23) == 3
(7^4 mod 23) == (9 mod 23) == 9
(7^8 mod 23) == (81 mod 23) == 12
(7^16 mod 23) == (144 mod 23) == 6
(7^24 mod 23) == (7^16 * 7^8 mod 23) == (6*12 mod 23) = 3
(7^25 mod 23) == (3*7 mod 23) == 21
"""

def mod_exp(x,y,N):
    # input: n-bit integers x,y,N≥0
    # output: x^y mod N
    if y == 0: return 1
    z = mod_exp(x, y//2, N)
    if y & 1 == 0: # last bit of y
        return z**2 % N
    else:
        return x*z**2 % N

if __name__ == '__main__':
    r = mod_exp(7, 25, 23)
    print(r)



