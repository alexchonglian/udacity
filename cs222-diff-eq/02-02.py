# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
import matplotlib.pyplot
import numpy

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    angle = 2 * math.pi / num_steps
    ###Your code here.
    for i in range(num_steps+1):
        cos = math.cos(angle*i)
        sin = math.sin(angle*i)
        x[i, 0] = moon_distance * cos
        x[i, 1] = moon_distance * sin
    
    return x

def orbit2():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    ###Your code here.
    theta = numpy.linspace(0, 2*math.pi, num_steps+1)
    x[:, 0] = moon_distance * numpy.cos(theta)
    x[:, 1] = moon_distance * numpy.sin(theta)
    return x

def orbit3():
    num_steps = 50
    theta = numpy.linspace(0, 2*math.pi, num_steps+1)
    x = moon_distance * numpy.column_stack((numpy.cos(theta), numpy.sin(theta)))
    return x

def running_time():
    from time import time
    t1 = time()
    for i in range(1000):x = orbit()
    t2 = time()
    for i in range(1000):x = orbit2()
    t3 = time()
    for i in range(1000):x = orbit3()
    t4 = time()
    # tested num_steps = 5000
    print t2-t1 #2.8551530838
    print t3-t2 #0.154500961304
    print t4-t3 #0.154740095139

x = orbit3()

def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()

plot_me()

