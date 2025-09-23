from data.terrain import TerrainType
from typing import Iterator
from utils.mapGen import generateGrid
import random


# grid containing TerrainType object from terrains dict
class TerrainGrid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.grid: list[list[TerrainType]] = generateGrid(width, height)

    
    def inBounds(self, x, y):
        return (x in range(self.width)) and (y in range(self.height))


    # starts at 0, 0 at top left
    def getTile(self, x, y):
        if not self.inBounds(x, y):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")
        
        return self.grid[y][x]
    

    def regenerate(self):
        random.seed()
        self.grid = generateGrid(self.width, self.height)

    def tiles(self) -> Iterator[tuple[TerrainType, int, int]]:
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                yield (tile, x, y)