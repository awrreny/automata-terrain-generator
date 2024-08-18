import pygame as pg
from settings import *
import scenes.battle
import renderer.drawGrid


def main():
    pg.init()


    TILE_FONT = pg.font.SysFont(None, TILE_TEXT_SIZE)
    
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # pg.mixer.init() for sound
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    grid = scenes.battle.Grid(12, 8)

    while True:
        renderer.drawGrid.draw_grid(grid, screen, TILE_FONT)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
