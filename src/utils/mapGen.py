import random
from copy import deepcopy
from time import sleep
from utils.debug import printgrid
from utils.neighbours import get_neighbour_proportion, NeighbourStrategy
from data.terrain import terrains
from data.terrainconfigs import TERRAIN_CONFIGS

# to run directly, python -m utils.mapGen
def automataGen(width, height, initial_density, survival_threshold = 0.4, birth_threshold = 0.4, 
                iterations=1, log=False, neighbour_strategy=NeighbourStrategy.WEIGHTED_DISTANCE):
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
                neighbour_proportion = get_neighbour_proportion(grid_snapshot, x, y, neighbour_strategy)

                if grid_snapshot[y][x]:
                    grid[y][x] = 1 if neighbour_proportion > scaled_survival_threshold else 0
                else:
                    grid[y][x] = 1 if neighbour_proportion > scaled_birth_threshold else 0
        
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




def generateGrid(width, height, log=False):
    config = random.choice(TERRAIN_CONFIGS)
    grid = [
        [
            terrains[config["background"]]
            for x in range(width)
        ]
        for y in range(height)
    ]

    for overlay in config["overlays"]:
        if log:
            sleep(1)

        automata_params = {k: v for k, v in overlay.items() if k != "terrain_type"}
        overlay_grid = automataGen(width, height, log=log, **automata_params)

        grid = applyGrid(grid, terrains[overlay["terrain_type"]], overlay_grid)

    return grid
