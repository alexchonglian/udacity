# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    height, width = len(grid), len(grid[0])
    values = [[99 for _ in xrange(width)] for _ in xrange(height)]
    xg, yg = goal
    grid[xg][yg] = -1
    values[xg][yg] = 0
    frontier = [[0, xg, yg]]
    while len(frontier) != 0:
        frontier.sort(reverse=True)
        current = frontier.pop()
        c, x, y = current
        for d in delta:
            dx, dy = d
            xp, yp = x-dx, y-dy
            if xp>=0 and xp<height and yp>=0 and yp<width and grid[xp][yp] == 0:
                frontier.append([c+cost, xp, yp])
                values[xp][yp] = c+cost
                grid[xp][yp] = -1
    return values

if __name__ == '__main__':
    values = compute_value(grid,goal,cost)
    for v in values: print(v)

