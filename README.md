# Automata Terrain Generator

Procedural 2D terrain generation using cellular automata rules (written in Python with Pygame).

## How To Use

Run with `python src/entry.py` from the project root.

-   `Space` to regenerate the terrain instantly.
-   `L` to regenerate terrain and watch each cellular automata pass, animated step-by-step in the terminal.
-   `Esc` or close window to exit.

## Change grid size

Use command line arguments to change the dimensions of the terrain grid. For example `python src/entry.py -W 50 -H 50 -T 20`

Run `python src/entry.py -h` to see all available options.

## How It Works

Each map is built from a randomly chosen configuration in `src/data/terrainconfigs.py`.

1. A base/background terrain type fills the whole grid.
2. Each overlay entry defines how a terrain type will be overlaid onto the grid (forest, sea, mountains, etc.).
3. For every overlay:
    - A binary grid is initialised with `initial_density` probability of 1s.
    - For up to `iterations` steps, cells are born or survive based on what proportion of their neighbours are alive.
    - Automata rules (thresholds for living/being born) are dynamically scaled toward the target density to keep distribution stable.
    - The result (where value == 1) is painted onto the main terrain grid using the specified terrain type.

## Customising Terrain Types

Add or edit terrain definitions in `src/data/terrain.py`:

```python
terrains["lava"] = TerrainType(
    name="lava",
    bg_colour=RED.brighten(0.2),
    icon_text="~",
    text_colour=RED.darken()
)
```

Properties:

-   `name`: identifier, matching keys in `terrainconfigs.py`
-   `bg_colour`: background colour (see helpers in `utils/colour.py`)
-   `icon_text`: small overlay text drawn inside the tile
-   `text_colour`: colour for the icon text

## Customising Generation Layers

Edit `src/data/terrainconfigs.py`. Each element of `TERRAIN_CONFIGS` is a possible map recipe randomly selected on generation:

```python
TERRAIN_CONFIGS = [
    {
        "background": "grass",
        "overlays": [
            {
                "terrain_type": "forest",
                "initial_density": 0.45,
                "survival_threshold": 0.3,
                "birth_threshold": 0.65,
                "iterations": 25,
                "neighbour_strategy": NeighbourStrategy.WEIGHTED_DISTANCE
            }
        ]
    }
]
```

Field meanings:

-   `background`: key from `terrains`
-   `terrain_type`: overlay terrain key to apply where the automaton grid has 1s
-   `initial_density`: starting proportion of alive cells (also target density)
-   `survival_threshold`: minimum neighbour proportion for an alive cell to stay alive
-   `birth_threshold`: minimum neighbour proportion for a dead cell to become alive
-   `iterations`: maximum automata steps (stops early if stable)
-   `neighbour_strategy`: enum controlling how neighbours are counted / weighted

Note that `survival_threshold` and `birth_threshold` are scaled dynamically during generation to keep the proportion of alive cells close to `initial_density`.
