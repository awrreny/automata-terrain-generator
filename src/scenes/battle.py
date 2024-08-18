from data.terrain import terrains


class Tile:
    def __init__(self, terrain="grass") -> None:
        if terrain not in terrains.keys():
            raise ValueError(f"")
        self.terrainData = terrains[terrain]

        # object on the tile e.g player unit, enemy unit, tetra (blockade)
        self.object = None


# grid is a 2D list containing Tile objects
class Grid:
    def __init__(self, width, height, defaultTerrainType="grass") -> None:
        self.grid = [
            [
                Tile(defaultTerrainType)
                for j in range(width)
            ]
            for i in range(height)
        ]


    # starts at 0, 0 at top left
    def getTileByCoords(self, x, y):
        if (x not in range(self.width)) or (y not in range(self.height)):
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")
        
        return self.grid[y][x]