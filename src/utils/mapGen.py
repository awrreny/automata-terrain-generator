import random
from copy import deepcopy
from time import sleep
from utils.debug import printgrid
from data.terrain import terrains

# to run directly, python -m utils.mapGen

def inBounds(x, y, width, height):
    return (x in range(width)) and (y in range(height))


def getNeighbourProportion(grid, x, y, radius = 3):
    """
    Returns the proportion of neighbours (within a given radius) that are set to 1, weighted by euclidean distance (closer = more weight)
    """
    height = len(grid)
    width = len(grid[0])
    total_weight = 0
    active_neighbor_weight = 0
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):

            if dx == 0 and dy == 0: continue
            if not inBounds(x+dx, y+dy, width, height): continue

            weight = (dx*dx + dy*dy)**(-0.5)
            total_weight += weight
            if grid[y+dy][x+dx]:
                active_neighbor_weight += weight

    if total_weight == 0:
        return 0

    return active_neighbor_weight / total_weight
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


def automataGen(width, height, initial_density, survival_threshold = 0.4, birth_threshold = 0.4, iterations=1, log=False):
    grid = [
        [
            1 if random.random() < initial_density else 0
            for j in range(width)
        ]
        for i in range(height)
    ]

    for _ in range(iterations):
        if log:
            print()
            printgrid(grid, binary=True)
            print("-"*100,end="")

            # to make the generation process visible
            sleep(0.1)

        grid_snapshot = deepcopy(grid)

        current_filled_ratio = sum(sum(row) for row in grid) / (width*height)

        # scales automata rules to encourage current_filled_ratio to be closer to initial_density
        scaled_survival_threshold = (survival_threshold/initial_density) * current_filled_ratio
        scaled_birth_threshold = (birth_threshold/initial_density) * current_filled_ratio

        for y in range(height):
            for x in range(width):
                neighbourProportion = getNeighbourProportion(grid_snapshot, x, y)

                if grid_snapshot[y][x]:
                    grid[y][x] = 1 if neighbourProportion > scaled_survival_threshold else 0
                else:
                    grid[y][x] = 1 if neighbourProportion > scaled_birth_threshold else 0
        
        if grid == grid_snapshot:  # no change in an iteration
            break

    if log:
        print()

    return grid
    

def applyGrid(grid, terrainType, bgrid):
    """
    Given a terrain grid, a binary grid, and a terrain type, returns a new grid which is the binary grid 'overlayed' onto the original grid, using the terrain type
    """
    for y, row in enumerate(bgrid):
        for x, tile in enumerate(row):
            if tile==1: 
                grid[y][x] = terrainType
    return grid




def generateGrid(width, height):
    
    grid = [
        [
            terrains["grass"]
            for x in range(width)
        ]
        for y in range(height)
    ]


    forestGrid = automataGen(width, height, 0.45,
                             survival_threshold=0.3,
                             birth_threshold=0.65,
                             iterations=25,
                             log=True)
    grid = applyGrid(grid, terrains["forest"], forestGrid)


    seaGrid = automataGen(width, height, 0.09,
                             survival_threshold=0.1,
                             birth_threshold=0.35,
                             iterations=25,
                             log=True)
    grid = applyGrid(grid, terrains["sea"], seaGrid)

    return grid
