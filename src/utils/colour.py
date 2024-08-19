# each colour is a 3-tuple (R, G, B)
import pygame as pg



class ColorMore(pg.Color):
    _WHITE = pg.Color(255, 255, 255)
    _BLACK = pg.Color(0, 0, 0)

    def brighten(self, factor=0.1):
        return self.lerp(ColorMore._WHITE, factor)


    def darken(self, factor=0.1):
        return self.lerp(ColorMore._BLACK, factor)


    def desaturate(self, factor=0.1):
        return self.lerp(self.grayscale(), factor)


WHITE = ColorMore(255, 255, 255)
BLACK = ColorMore(0, 0, 0)
RED = ColorMore(255, 0, 0)
GREEN = ColorMore(0, 255, 0)
BLUE = ColorMore(0, 0, 255)


# idea: blending colours for borders?
