from utils.grid import TerrainGrid
from settings import TILE_SIZE
from utils.colour import BLACK
import pygame as pg



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
        textRect.center = tileRect.center

        screen.blit(textSurface, textRect)



