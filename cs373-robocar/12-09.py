# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    height, width = len(grid), len(grid[0])
    expand = [[0 if grid[i][j]==0 else -1 for j in xrange(width)] for i in xrange(height)]
    x, y = init
    grid[x][y] = -1
    count = 0
    frontier = [[0,x,y]]
    while len(frontier) != 0:
        frontier.sort(reverse=True)
        current = frontier.pop()
        c, x, y = current
        if [x, y] == goal:
            return expand
        for d in delta:
            dx, dy = d
            xn, yn = x+dx, y+dy
            if xn>=0 and xn<height and yn>=0 and yn<width and grid[xn][yn]==0:
                count += 1
                cn = c+cost
                frontier.append([cn, xn, yn])
                grid[xn][yn] = -1
                expand[xn][yn] = count
    return expand

if __name__ == '__main__':
    expand = search(grid, init, goal, cost)
    for expd in expand:
        print expd