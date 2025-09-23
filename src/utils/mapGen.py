import random
from copy import deepcopy
from time import sleep


if __name__ == "__main__":
    from debug import printgrid
elif __name__ == "utils.mapGen":
    # if opened from entry.py
    from utils.debug import printgrid
    from data.terrain import terrains
else:
    raise Exception("yeahh")


def inBounds(x, y, width, height):
    return (x in range(width)) and (y in range(height))


def getNeighbourProportion(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    total = 0
    count = 0
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            if dx == 0 and dy == 0: continue
            if not inBounds(x+dx, y+dy, width, height): continue

            weight = (dx*dx + dy*dy)**(-0.5)
            total += weight
            if grid[y+dy][x+dx]:
                count += weight

    return count/total
# king-move neighbours
# def neighbours(grid, x, y):
#     height = len(grid)
#     width = len(grid[0])
#     for dx in (-1, 0, 1):
#         for dy in (-1, 0, 1):
#             if dx == 0 and dy == 0: continue
#             if not inBounds(x+dx, y+dy, width, height): continue
#             yield grid[y+dy][x+dx]



# # manhattan unit neighbours
# def neighbours(grid, x, y):
#     height = len(grid)
#     width = len(grid[0])
#     for x, y in (0, 1), (0, -1), (-1, 0), (1, 0):
#         if not inBounds(x, y, width, height): continue
#         yield grid[y][x]

# mix of both with closer being weighted more
# def neighbours(grid, x, y):
#     height = len(grid)
#     width = len(grid[0])
#     for dx in (-1, 0, 1):
#         for dy in (-1, 0, 1):
#             if dx == 0 and dy == 0: continue
#             if not inBounds(x+dx, y+dy, width, height): continue
#             if abs(dy+dx) == 2 and random.random() < 0.5: continue
#             yield grid[y+dy][x+dx]


def automataGen(width, height, initialChance, stayAliveProp = 0.4, birthProp = 0.4, iterations=1, log=False):
    # generate random grid
    grid = [
        [
            1 if random.random() < initialChance else 0
            for j in range(width)
        ]
        for i in range(height)
    ]


    for i in range(iterations):
        if log:
            print()
            printgrid(grid, binary=True)
            print("-"*100,end="")

            sleep(0.1)

        gridSnapshot = deepcopy(grid)

        filledProportion = (1/(width*height)) * sum(sum(row) for row in grid)

        # scales automata rules to encourage filledProportion to be closer to initialChance
        stayAlivePropScaled = (stayAliveProp/initialChance) * filledProportion
        birthPropScaled = (birthProp/initialChance) * filledProportion

        for y in range(height):
            for x in range(width):
                # apply automata rules
                # total = 0
                # count = 0
                # for tile in neighbours(gridSnapshot, x, y):
                #     if tile == 1:
                #         count += 1
                #     total += 1
                neighbourProportion = getNeighbourProportion(gridSnapshot, x, y)

                if gridSnapshot[y][x]:
                    grid[y][x] = 1 if neighbourProportion > stayAlivePropScaled else 0
                else:
                    grid[y][x] = 1 if neighbourProportion > birthPropScaled else 0
        
        if grid == gridSnapshot:  # no change in an iteration
            break

    if log:
        print()

    return grid
    

# given a grid, a binary grid, and a terrain type, returns a new grid which is the binary grid 'overlayed' onto the original grid, using the terrain type
def applyGrid(grid, terrainType, bgrid):
    for y, row in enumerate(bgrid):
        for x, tile in enumerate(row):
            if tile==1: 
                grid[y][x] = terrainType
    return grid




def generateGrid(width, height, safeCorners=False, safeCornerSize=3, forestInitialChance=0.4, forestReqProportion=0.4, forestIterations=1, lakeSpawnTries=3, lakeClusterSize=12):
    
    grid = [
        [
            terrains["grass"]
            for x in range(width)
        ]
        for y in range(height)
    ]


    forestGrid = automataGen(width, height, 0.45,
                             stayAliveProp=0.3,
                             birthProp=0.65,
                             iterations=25,
                             log=True)
    grid = applyGrid(grid, terrains["forest"], forestGrid)


    seaGrid = automataGen(width, height, 0.09,
                             stayAliveProp=0.1,
                             birthProp=0.35,
                             iterations=25)
    grid = applyGrid(grid, terrains["sea"], seaGrid)

    return grid



    


# printgrid(automataGen(20, 10, 0.45,
#                       stayAliveProp=0.3,
#                       birthProp=0.65,
#                       iterations=100))

# printgrid(automataGen(20, 10, 0.5,
#                       stayAliveProp=0.6,
#                       birthProp=0.4,
#                       iterations=50))
# printgrid(automataGen(20, 10, 0.5,
#                       stayAliveProp=0.5,
#                       birthProp=0.5,
#                       iterations=50))


# printgrid(automataGen(20, 10, 0.09,
#                       stayAliveProp=0.1,
#                       birthProp=0.35,
#                       iterations=100,
#                       log=True))


# printgrid(generateGrid(20,10))