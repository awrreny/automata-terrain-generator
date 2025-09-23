from utils.neighbours import NeighbourStrategy

DEFAULT_TERRAIN_CONFIG = {
    "background": "grass",
    "overlays": [
        {
            "terrain_type": "forest",
            "initial_density": 0.45,
            "survival_threshold": 0.3,
            "birth_threshold": 0.65,
            "iterations": 25,
            "neighbour_strategy": NeighbourStrategy.WEIGHTED_DISTANCE
        },
        {
            "terrain_type": "sea",
            "initial_density": 0.09,
            "survival_threshold": 0.1,
            "birth_threshold": 0.35,
            "iterations": 25,
            "neighbour_strategy": NeighbourStrategy.WEIGHTED_DISTANCE
        }
    ]
}

DESERT_TERRAIN_CONFIG = {
    "background": "sand",
    "overlays": [
        {
            "terrain_type": "mountain",
            "initial_density": 0.2,
            "survival_threshold": 0.2,
            "birth_threshold": 0.5,
            "iterations": 10,
            "neighbour_strategy": NeighbourStrategy.WEIGHTED_DISTANCE
        }
    ]
}