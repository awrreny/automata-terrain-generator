from data.terrain import terrains
from typing import Tuple, Generator
from utils.mapGen import generateGrid
import random


# grid containing TerrainType object from terrains dict
class TerrainGrid:
    def __init__(self, width, height, defaultTerrainType="forest") -> None:
        self.width = width
        self.height = height

        # self.grid = [
        #     [
        #         terrains[random.choice(["grass", "grass", "grass", "forest", "sea"])]
        #         for j in range(width)
        #     ]
        #     for i in range(height)
        # ]
        self.grid = generateGrid(width, height)


    
    def inBounds(self, x, y):
        return (x in range(self.width)) and (y in range(self.height))


    # starts at 0, 0 at top left
    def getTileByCoords(self, x, y):
        if not self.inBounds(x, y):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")
        
        return self.grid[y][x]
    

    def tiles(self) -> Generator[Tuple[int, int, str], None, None]:
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                yield (tile, x, y)