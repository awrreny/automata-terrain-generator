import pygame as pg
from settings import *
import utils.grid
import renderer.drawGrid


def main():
    pg.init()

    TILE_FONT = pg.font.SysFont(None, TILE_TEXT_SIZE)
    
    screen = pg.display.set_mode((DEFAULT_GRID_WIDTH * DEFAULT_TILE_SIZE, DEFAULT_GRID_HEIGHT * DEFAULT_TILE_SIZE))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    grid = utils.grid.TerrainGrid(DEFAULT_GRID_WIDTH, DEFAULT_GRID_HEIGHT)

    while True:
        renderer.drawGrid.draw_terrain(grid, screen, TILE_FONT)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    grid.regenerate()
                elif event.key == pg.K_l:
                    grid.regenerate(log=True)
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
