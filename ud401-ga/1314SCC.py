from collections import defaultdict

def edges_to_adjlist(edges):
    adjlist = defaultdict(list)
    for f,t in edges:
        adjlist[f].append(t)
    return adjlist

if __name__ == '__main__':
    edges0 = [
        ('A','B'),('B','C'),('B','D'),('B','E'),
        ('C','F'),('E','B'),('E','L'),
        ('F','G'),('F','I'),('G','C'),('G','F'),
        ('H','I'),('H','J'),('I','J'),
        ('J','H'),('J','K'),('K','L'),('L','I')
    ]