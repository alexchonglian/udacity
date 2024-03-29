# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------
import matplotlib.pyplot as plt
from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

def plotpaths(path):
    x, y = zip(*path)
    plt.scatter(x, y)
    plt.show()

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):
    # Make a deep copy of path into newpath
    newpath = deepcopy(path)
    #######################
    ### ENTER CODE HERE ###
    #######################
    length, dim = len(path), len(path[0])
    change = tolerance+1.0
    while change > tolerance:
        change = 0.0
        for i in range(1, length-1):
            for j in range(dim):
                xcurr = path[i][j]
                yprev, ycurr, ynext = newpath[i-1][j], newpath[i][j], newpath[i+1][j]
                update = weight_data * (xcurr - ycurr) + weight_smooth * (ynext+yprev-2.0*ycurr)
                newpath[i][j] += update
                change += abs(update)
    return newpath # Leave this line for the grader!

smooth_path = smooth(path)
plotpaths(smooth_path)
printpaths(path, smooth_path)

