from utils.grid import TerrainGrid
from settings import TILE_SIZE
from utils.colour import BLACK
from typing import Tuple
import pygame as pg
import random

def randomise_pos(x, y, seed, factor=12):
    random.seed(seed)
    return (
        x + random.randint(-TILE_SIZE//factor, TILE_SIZE//factor),
        y + random.randint(-TILE_SIZE//factor, TILE_SIZE//factor),
    )



def draw_terrain(grid: TerrainGrid, screen, font: pg.font.Font, startCoords=(0,0)):
    startX, startY = startCoords
    for terrain, x, y in grid.tiles():
        bgColour = terrain.bg_colour
        textColour= terrain.text_colour
        text = terrain.icon_text

        tileRect = pg.Rect(startX + x*TILE_SIZE, startY + y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pg.draw.rect(screen, bgColour, tileRect)

        pg.draw.rect(screen, bgColour.darken(0.015), tileRect, 1)

        textSurface = font.render(text, True, textColour)
        textRect = textSurface.get_rect()

        # slightly randomise position. this seed will be different for different tiles but the same for the same tile
        textRect.center = randomise_pos(*tileRect.center, (x<<8)^y)

        screen.blit(textSurface, textRect)



