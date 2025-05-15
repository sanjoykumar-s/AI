import copy

def isGoal (grid, goal):
    return grid == goal


def huristic(grid, goal, g):
    count = 0
    for i in range(len(goal)):
        for j in range(len(goal[i])):
            if goal[i][j]!=0 and goal[i][j]!=grid[i][j]:
                count = count + 1
    return count+g


def printMat(grid):
    for i in range(len(grid)):
        print("|", end="")
        for j in range(len(grid[i])):
            print(grid[i][j], end="|")
        print()

def findPoint(tem):
    for i in range(len(tem)):
        for j in range(len(tem[i])):
            if tem[i][j] == 0:
                return (i,j)
            

def solve(grid, goal, g, blk):
    global distanceFromStart

    if g>50:
        print("Goal Not Possible")
        return
    if g==1:
        print("Initial State:")
    else:
        print("Current State:")
    printMat(grid)
    print()

    if isGoal(grid, goal):
        distanceFromStart = g
        return

    tem = copy.deepcopy(grid)
    (i,j) = findPoint(tem)
    dir = (0,0)
    f = 10000
    #up
    if i-1 >= 0 and blk!=(1,0):
        xx = tem[i][j]
        tem[i][j] = tem[i-1][j]
        tem[i-1][j] = xx
        print("UP:")
        printMat(tem)
        cost = huristic(tem, goal, g)
        print(f"Cost of this move: {cost}")
        print()
        if cost<f:
            f = cost
            dir = (-1,0)

    #down
    tem = copy.deepcopy(grid)
    (i,j) = findPoint(tem)
    if i+1 < len(grid) and blk!=(-1,0):
        xx = tem[i][j]
        tem[i][j] = tem[i+1][j]
        tem[i+1][j] = xx
        print("Down:")
        printMat(tem)
        cost = huristic(tem, goal, g)
        print(f"Cost of this move: {cost}")
        print()
        if cost<f:
            f = cost
            dir = (1,0)

    #left
    tem = copy.deepcopy(grid)
    (i,j) = findPoint(tem)
    if j-1 >= 0 and blk!=(0,1):
        xx = tem[i][j]
        tem[i][j] = tem[i][j-1]
        tem[i][j-1] = xx
        print("Left:")
        printMat(tem)
        cost = huristic(tem, goal, g)
        print(f"Cost of this move: {cost}")
        print()
        if cost<f:
            f = cost
            dir = (0, -1)

    #Right
    tem = copy.deepcopy(grid)
    (i,j) = findPoint(tem)
    if j+1 <len(grid[0]) and blk!=(0,-1):
        xx = tem[i][j]
        tem[i][j] = tem[i][j+1]
        tem[i][j+1] = xx
        print("Right:")
        printMat(tem)
        cost = huristic(tem, goal, g)
        print(f"Cost of this move: {cost}")
        print()
        if cost<f:
            f = cost
            dir = (0, 1)


    tem = copy.deepcopy(grid)
    tem[i][j], tem[i+dir[0]][j+dir[1]] = tem[i+dir[0]][j+dir[1]], tem[i][j]

    selection = ""
    if dir[0] == -1:
        selection = "UP   "
    elif dir[0] == 1:
        selection = "Down "
    elif dir[1] == -1:
        selection = "Left "
    else:
        selection = "Right"

    print("--------------------------------")
    print(f"| Smallest Selection Cost: {f}   |")
    print("|------------------------------|")
    print(f"| Optimal Selected Move: {selection} |")
    print("--------------------------------")
    print()

    solve(tem, goal, g+1, dir)



grid = [[2,8,3],
        [1,6,4],
        [7,0,5]]
goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]
blk = (0,0)


print("Goal State:")
printMat(goal)
print()

solve(grid,goal,1, blk)

if distanceFromStart < 50:
    print("----------------")
    print("| Goal Reached |")
    print("|--------------|")
    print(f"| G(n) = {distanceFromStart}     |")
    print("----------------")
else:
    print(" Sorry... Reaching Goal is not possible :(")