from utils.grid import TerrainGrid
import pygame as pg
from pygame.font import Font
import random

rng = random.Random()

def randomise_position(coords: tuple[int, int], stddev: float) -> tuple[int, int]:
    x, y = coords
    seed = (x<<16)|y
    rng.seed(seed)
    return (
        int(random.gauss(x, stddev)),
        int(random.gauss(y, stddev)),
    )


class GridDrawer():
    def __init__(self, screen: pg.Surface, font: Font, grid: TerrainGrid, 
                 tile_size: int, offset: tuple[int, int] = (0, 0)) -> None:
        self.screen = screen
        self.font = font
        self.grid = grid
        self.tile_size = tile_size
        self.offset = offset

    def draw(self) -> None:
        start_x, start_y = self.offset

        for terrain, x, y in self.grid.tiles():
            bg_colour = terrain.bg_colour
            text_colour= terrain.text_colour
            tile_text = terrain.icon_text

            tile_x = start_x + x * self.tile_size
            tile_y = start_y + y * self.tile_size
            tile_rect = pg.Rect(tile_x, tile_y, self.tile_size, self.tile_size)

            # main tile
            pg.draw.rect(self.screen, bg_colour, tile_rect)
            # border
            pg.draw.rect(self.screen, bg_colour.darken(0.015), tile_rect, 1)

            # text
            text_surface = self.font.render(tile_text, True, text_colour)
            text_rect = text_surface.get_rect()
            text_rect.center = randomise_position(tile_rect.center, self.tile_size//25)
            
            self.screen.blit(text_surface, text_rect)
