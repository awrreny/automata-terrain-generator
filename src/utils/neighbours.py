"""
Grid neighbour calculation strategies for cellular automata calculations.
"""
import random
from enum import Enum
from typing import Iterator


def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    """Check if coordinates are within grid boundaries."""
    return (x in range(width)) and (y in range(height))


class NeighbourStrategy(Enum):
    WEIGHTED_DISTANCE = "weighted_distance"
    KING_MOVE = "king_move" 
    MANHATTAN = "manhattan"
    MIXED = "mixed"


def get_neighbours_king_move(grid: list[list[int]], x: int, y: int) -> Iterator[int]:
    """8-directional neighbours (including diagonals)"""
    height, width = len(grid), len(grid[0])
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0: 
                continue
            if in_bounds(x+dx, y+dy, width, height):
                yield grid[y+dy][x+dx]


def get_neighbours_manhattan(grid: list[list[int]], x: int, y: int) -> Iterator[int]:
    """4-directional neighbours (no diagonals)"""
    height, width = len(grid), len(grid[0])
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if in_bounds(x+dx, y+dy, width, height):
            yield grid[y+dy][x+dx]


def get_neighbours_mixed(grid: list[list[int]], x: int, y: int) -> Iterator[int]:
    """King-move with 50% chance to skip diagonals for irregular patterns"""
    height, width = len(grid), len(grid[0])
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0: 
                continue
            if not in_bounds(x+dx, y+dy, width, height): 
                continue
            # Skip diagonals randomly for irregular patterns
            if abs(dx) + abs(dy) == 2 and random.random() < 0.5: 
                continue
            yield grid[y+dy][x+dx]


def get_weighted_neighbour_proportion(grid: list[list[int]], x: int, y: int, radius: int = 3) -> float:
    """
    Returns proportion of neighbours weighted by euclidean distance.
    Closer neighbours have more influence on the result.
    """
    height, width = len(grid), len(grid[0])
    total_weight = 0
    active_neighbour_weight = 0
    
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            if dx == 0 and dy == 0: 
                continue
            if not in_bounds(x+dx, y+dy, width, height): 
                continue

            weight = (dx*dx + dy*dy)**(-0.5)
            total_weight += weight
            if grid[y+dy][x+dx]:
                active_neighbour_weight += weight

    return active_neighbour_weight / total_weight if total_weight > 0 else 0


def get_neighbour_proportion(grid: list[list[int]], x: int, y: int, 
                          strategy: NeighbourStrategy = NeighbourStrategy.WEIGHTED_DISTANCE,
                          radius: int = 3) -> float:
    """Get neighbour proportion using specified strategy."""
    if strategy == NeighbourStrategy.WEIGHTED_DISTANCE:
        return get_weighted_neighbour_proportion(grid, x, y, radius)
    elif strategy == NeighbourStrategy.KING_MOVE:
        neighbors = list(get_neighbours_king_move(grid, x, y))
    elif strategy == NeighbourStrategy.MANHATTAN:
        neighbors = list(get_neighbours_manhattan(grid, x, y))
    elif strategy == NeighbourStrategy.MIXED:
        neighbors = list(get_neighbours_mixed(grid, x, y))
    else:
        raise ValueError(f"Unknown neighbor strategy: {strategy}")
    
    return sum(neighbors) / len(neighbors) if neighbors else 0
