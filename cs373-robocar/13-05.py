# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    # Probability(stepping left) = prob(stepping right) = failure_prob
    failure_prob = (1.0 - success_prob)/2.0
    height, width = len(grid), len(grid[0])
    values = [[collision_cost for col in range(width)] for row in range(height)]
    policy = [[' ' for col in range(width)] for row in range(height)]
    def cost(x,y,d):
        dx, dy = d
        x, y = x+dx, y+dy
        if x>=0 and x<height and y>=0 and y<width and grid[x][y] == 0:
            return values[x][y]
        else: return collision_cost
    change = True
    while change:
        change = False
        for x in range(height):
            for y in range(width):
                if goal == [x, y] and values[x][y] > 0.0:
                    values[x][y] = 0.0
                    policy[x][y] = '*'
                    change = True
                elif grid[x][y] == 0:
                    for i in range(4):
                        delts = [delta[i-1],   delta[i],     delta[(i+1)%4]]
                        probs = [failure_prob, success_prob, failure_prob]
                        new_cost = sum(p*cost(x,y,d) for d,p in zip(delts, probs)) + cost_step
                        if new_cost < values[x][y]:
                            values[x][y] = new_cost
                            policy[x][y] = delta_name[i]
                            change = True
    return values, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------
cost_step = 1
collision_cost = 1000
success_prob = 0.5

grid1 = [[0,0,0],
        [0,0,0]]
goal1 = [0, 2]
value,policy = stochastic_value(grid1,goal1,cost_step,collision_cost,success_prob)
for row in value:
    print row
for row in policy:
    print row
# Expected outputs:
#
#[580.2424242424242, 355.6565656565657, 0.0]
#[605.6565656565657, 419.1919191919193, 355.7979797979798]
#
#['>', 'v', '*']
#['>', '^', '^']

grid2 = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal2 = [0, 3] # Goal is in top right corner
value,policy = stochastic_value(grid2,goal2,cost_step,collision_cost,success_prob)
for row in value:
    print row
for row in policy:
    print row


# Expected outputs:
#
#[471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
#[334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977], 
#[398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738], 
#[700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
