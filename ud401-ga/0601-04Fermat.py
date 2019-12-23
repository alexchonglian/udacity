"""
Fermat's little Theorem

If p is prime then for every 1≤z≤p-1
z^(p-1) ≡ 1 mod p
gcd(z,p) = 1

Basis of RSA algo

Basis of primality test algo

Proof:
    S = [1,2,3,...,p-1]
    S'= [zS mod p]
      = [z%p, 2z%p, 3z%p, ... , (p-1)z%p]

Example: p=7, z=4
    S = [1,2,3,4,5,6]
    S'= [4,1,5,2,6,3]
    S == S'

Proof S = S'
    show elements of S' are distinct and non-zero
    proof elements of S' are distinct, by contradiction
        suppose for some i≠j, iz ≡ jz mod p
        p is prime => z^-1 mod p exists
        i*z*z^-1 ≡ j*z*z^-1 mod p
        thus i ≡ j mod p, contradict i≠j
    proof elements of S' are non-zero, by contradiction
        suppose iz≡0 mod p

"""