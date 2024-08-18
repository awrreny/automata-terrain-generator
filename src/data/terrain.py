from settings import *
from utils.colour import darken, brighten, desaturate


terrains = {
    "forest": {
        "slowdown_factor": 2,  # in DT, this factor is different for diff. move types. especially no slowdown for flying units
        "defence_bonus": 2,  # maybe weaken bonus for flying units

        # map icon display
        "bg_colour": darken(desaturate(GREEN)),
        "text_colour": darken(darken(desaturate(GREEN))),
        "text": "/\\/\\"
    },
    "grass": {
        "slowdown_factor": 0,
        "defence_bonus": 1,

        # map icon display
        "bg_colour": desaturate(GREEN),
        "text_colour": WHITE,
        "text": ""
    }
}