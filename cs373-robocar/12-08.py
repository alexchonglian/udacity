# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

grid2= [[0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    height, width = len(grid), len(grid[0])
    x, y = init
    grid[x][y] = -1
    frontier = [[0, x, y]]
    while len(frontier) != 0:
        frontier.sort(reverse=True)
        current = frontier.pop()
        c, x, y = current
        if [x,y] == goal:
            return current
        for d in delta:
            dx, dy = d
            xn, yn = x+dx, y+dy
            if xn>=0 and xn<height and yn>=0 and yn<width and grid[xn][yn]==0:
                cn = c+cost
                frontier.append([cn, xn, yn])
                grid[xn][yn] = -1 # mark visited on orig map
    return "fail"

if __name__ == '__main__':
    path = search(grid, init, goal, cost)
    print(path)
