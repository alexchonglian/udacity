# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    # Dijkstra, what about cycles?
    height, width = len(grid), len(grid[0])
    values = [[[float('inf') for _ in range(4)] for _ in range(width)] for _ in range(height)]
    froms = {} # (x1, y1, t1) => (x0, y0, t0, action)
    visited = {} # not used here
    x0, y0, t0 = init
    values[x0][y0][t0] = 0
    frontier = [[0, x0, y0, t0]]
    while len(frontier) != 0:
        frontier.sort()
        current = frontier.pop()
        c, x, y, t = current
        for idx in [0,1,2]:
            # calculate next state
            tn = (t+action[idx]) % 4
            dx, dy = forward[tn]
            cn, xn, yn = cost[idx]+c, x+dx, y+dy
            # if next state valid => update values, froms, frontier
            if xn>=0 and xn<height and yn>=0 and yn<width \
            and grid[xn][yn] == 0 and cn < values[xn][yn][tn]:
                values[xn][yn][tn] = cn
                froms[(xn,yn,tn)] = (x,y,t,action_name[idx])
                frontier.append([cn, xn, yn, tn])
    # backtracking
    #for v in values:print v
    policy2D = [[' ' for _ in range(width)] for _ in range(height)]
    xg, yg = goal
    policy2D[xg][yg] = '*'
    value_goal = values[xg][yg]
    tg = value_goal.index(min(value_goal))
    x,y,t = xg,yg,tg
    while (x,y,t) in froms:
        x,y,t,a = froms[(x,y,t)]
        policy2D[x][y] = a
    #for p in policy2D: print p
    return policy2D
"""
"""
def optimum_policy2D(grid,init,goal,cost):
    # Dynamic Programming
    height, width = len(grid), len(grid[0])
    values = [[[float('inf') for _ in range(4)] for _ in range(width)] for _ in range(height)]
    policy = [[[' ' for _ in range(4)] for _ in range(width)] for _ in range(height)]
    change = True
    while change:
        change = False
        for x in range(height):
            for y in range(width):
                for t in range(4):
                    if goal == [x,y] and values[x][y][t] > 0:
                        values[x][y][t] = 0
                        policy[x][y][t] = '*'
                        change = True
                    elif grid[x][y] == 0:
                        for i in range(3):
                            o2 = (t + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            if x2 >= 0 and x2 < height \
                            and y2 >= 0 and y2 < width and grid[x2][y2] == 0:
                                v2 = values[x2][y2][o2] + cost[i]
                                if v2 < values[x][y][t]:
                                    change = True
                                    values[x][y][t] = v2
                                    policy[x][y][t] = action_name[i]
    #for v in values:print v
    policy2D = [[' ' for _ in range(width)] for _ in range(height)]
    x,y,t = init
    policy2D[x][y] = policy[x][y][t]
    while policy[x][y][t] != '*':
        if policy[x][y][t] == '#':
            o2 = t
        elif policy[x][y][t] == 'R':
            o2 = (t - 1) % 4
        elif policy[x][y][t] == 'L':
            o2 = (t + 1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        t = o2
        policy2D[x][y] = policy[x][y][t]
    for p in policy2D: print p
    return policy2D

if __name__ == '__main__':
    optimum_policy2D(grid,init,goal,cost)
