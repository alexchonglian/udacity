import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        if v.dimension != self.dimension:
            raise ValueError('The dimension must match')
        return Vector([sum(i) for i in zip(self.coordinates, v.coordinates)])

    def scalar_mul(self, scalar):
        return Vector([i*scalar for i in self.coordinates])

    def mag(self):
        return math.sqrt( sum([i**2 for i in self.coordinates]) )

    def normalize(self):
        return Vector([i/self.mag() for i in self.coordinates])

if __name__ == '__main__':
    print Vector([-0.221, 7.437]).mag()
    print Vector([5.581, -2.136]).normalize()
    print Vector([8.813, -1.331, -6.247]).mag()
    print Vector([1.996, 3.108, -4.554]).normalize()
