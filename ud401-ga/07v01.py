"""
Hashing Outline

Balls into bins
    power of 2 choices

Chain hashing

Bloom filters


Hashing setup

Running example: unacceptable passwords
Huge set U = possible passwords
maintain S, subset of U, of unacceptable passwords

Query for x in U, is x in S?

Hash table H = [0,1, ..., n-1], array of linked lists
hash function h: U->H
h(x) random in [0,1, ..., n-1]

|U| = N, |H| = n, |S| = m

"""