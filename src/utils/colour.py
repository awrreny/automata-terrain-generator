# each colour is a 3-tuple (R, G, B)
from pygame import Color



class ColorMore(Color):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def brighten(self, factor: float = 0.1):
        return ColorMore(self.lerp(ColorMore.WHITE, factor))


    def darken(self, factor: float = 0.1):
        return ColorMore(self.lerp(ColorMore.BLACK, factor))


    def desaturate(self, factor: float = 0.1):
        return ColorMore(self.lerp(self.grayscale(), factor))


WHITE = ColorMore(255, 255, 255)
BLACK = ColorMore(0, 0, 0)
RED = ColorMore(255, 0, 0)
GREEN = ColorMore(0, 255, 0)
BLUE = ColorMore(0, 0, 255)
YELLOW = ColorMore(255, 255, 0)
ORANGE = ColorMore(255, 165, 0)


# idea: blending colours for borders?
