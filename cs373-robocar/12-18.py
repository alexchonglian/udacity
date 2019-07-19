# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    height, width = len(grid), len(grid[0])
    policy = [[' ' for _ in xrange(width)] for _ in xrange(height)]
    xg, yg = goal
    grid[xg][yg] = -1
    policy[xg][yg] = '*'
    frontier = [[0, xg, yg]]
    while len(frontier) != 0:
        frontier.sort(reverse=True)
        current = frontier.pop()
        c, x, y = current
        for i in xrange(len(delta)):
            dx, dy = delta[i]
            xp, yp = x-dx, y-dy
            if xp>=0 and xp<height and yp>=0 and yp<width and grid[xp][yp] == 0:
                frontier.append([c+cost, xp, yp])
                policy[xp][yp] = delta_name[i]
                grid[xp][yp] = -1
    return policy


if __name__ == '__main__':
    policy = optimum_policy(grid,goal,cost)
    for p in policy: print(p)