import pygame as pg
from settings import *
import utils.grid
import renderer.gridDrawer


def main():
    pg.init()

    TILE_FONT = pg.font.SysFont(None, TILE_TEXT_SIZE)
    
    screen = pg.display.set_mode((DEFAULT_GRID_WIDTH * DEFAULT_TILE_SIZE, DEFAULT_GRID_HEIGHT * DEFAULT_TILE_SIZE))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    grid = utils.grid.TerrainGrid(DEFAULT_GRID_WIDTH, DEFAULT_GRID_HEIGHT)

    grid_drawer = renderer.gridDrawer.GridDrawer(screen, TILE_FONT, grid, DEFAULT_TILE_SIZE)
    grid_drawer.draw()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    grid.regenerate()
                    grid_drawer.draw()
                elif event.key == pg.K_l:
                    grid.regenerate(log=True)
                    grid_drawer.draw()
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
