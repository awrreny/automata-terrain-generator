from settings import *
from utils.colour import *


GRASS_COLOUR = GREEN.desaturate(0.5)
WATER_COLOUR = BLUE.desaturate(0.3).brighten(0.4)

class TerrainType:
    def __init__(self, name: str, bg_colour, icon_text, text_colour)  -> None:
        self.name = name
        self.displayName = name.title()

        self.bg_colour = bg_colour
        self.icon_text = icon_text
        self.text_colour = text_colour
    

    def __repr__(self) -> str:
        return self.name[0].upper()


terrains = dict()

terrains["forest"] = TerrainType(
    name="forest",

    bg_colour=GRASS_COLOUR.darken(),
    icon_text="/\\ /\\",
    text_colour=GRASS_COLOUR.darken(0.2),
)

terrains["grass"] = TerrainType(
    name="grass",

    bg_colour=GRASS_COLOUR,
    icon_text="",
    text_colour=WHITE,
)

terrains["sea"] = TerrainType(
    name="sea",

    bg_colour=WATER_COLOUR,
    icon_text="~ ~",
    text_colour=WATER_COLOUR.darken()
)

