from data.terrain import terrains
from typing import Tuple, Generator
import random


# grid containing TerrainType object from terrains dict
class TerrainGrid:
    def __init__(self, width, height, defaultTerrainType="forest") -> None:
        self.grid = [
            [
                terrains[random.choice(["grass", "grass", "grass", "forest", "sea"])]
                for j in range(width)
            ]
            for i in range(height)
        ]
        self.width = width
        self.height = height


    # starts at 0, 0 at top left
    def getTileByCoords(self, x, y):
        if (x not in range(self.width)) or (y not in range(self.height)):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")
        
        return self.grid[y][x]
    

    def tiles(self) -> Generator[Tuple[int, int, str], None, None]:
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                yield (tile, x, y)