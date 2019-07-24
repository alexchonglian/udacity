# PROBLEM 2
#
# Modify the trajectory function below to 
# plot the trajectory of several particles. 
# Each trajectory starts at the point (0,0) 
# given initial speed in the direction 
# specified by the angle. Use the Forward 
# Euler Method to accomplish this.

import math
import matplotlib.pyplot
import numpy

h = 0.1 # s
g = 9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 20. # m / s

def trajectory():
    angles = numpy.linspace(20., 70., 6)

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        ###Your code here.
        v[0,0] = initial_speed * math.cos(math.pi *angle/180)
        v[0,1] = initial_speed * math.sin(math.pi *angle/180)
        for i in range(1, num_steps+1):
            x[i] = x[i-1] + h * v[i-1]
            v[i] = v[i-1] + h * acceleration
        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    matplotlib.pyplot.show()
    return x, v

trajectory()


