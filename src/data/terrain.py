from settings import *
from utils.colour import *


GRASS_COLOUR = GREEN.desaturate(0.5)


terrains = {
    "forest": {
        "slowdown_factor": 2,  # in DT, this factor is different for diff. move types. especially no slowdown for flying units
        "defence_bonus": 2,  # maybe weaken bonus for flying units

        # map icon display
        "bg_colour": GRASS_COLOUR.darken(),
        "text_colour": GRASS_COLOUR.darken(0.2),
        "text": "/\\ /\\"
    },
    "grass": {
        "slowdown_factor": 0,
        "defence_bonus": 1,

        # map icon display
        "bg_colour": GRASS_COLOUR,
        "text_colour": WHITE,
        "text": ""
    }
}