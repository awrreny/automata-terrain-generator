from scenes.battle import Grid, Tile
from settings import TILE_SIZE, BLACK
import pygame as pg

from utils.colour import darken


def draw_grid(grid: Grid, screen, font: pg.font.Font, startCoords=(0,0)):
    startX, startY = startCoords
    for tile, x, y in grid.tiles():
        bgColour = tile.terrainData["bg_colour"]
        textColour= tile.terrainData["text_colour"]
        text = tile.terrainData["text"]

        if tile.object is not None:
            pass
            # TODO

        tileRect = pg.Rect(startX + x*TILE_SIZE, startY + y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pg.draw.rect(screen, bgColour, tileRect)

        pg.draw.rect(screen, darken(bgColour, 0.015), tileRect, 1)

        textSurface = font.render(text, True, textColour)
        textRect = textSurface.get_rect()
        textRect.center = tileRect.center

        screen.blit(textSurface, textRect)



