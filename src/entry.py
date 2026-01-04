import pygame as pg
from settings import *
import utils.grid
import renderer.gridDrawer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", "--width", type=int, default=DEFAULT_GRID_WIDTH, help="Grid width in tiles")
parser.add_argument("-H", "--height", type=int, default=DEFAULT_GRID_HEIGHT, help="Grid height in tiles")
parser.add_argument("-T", "--tile-size", type=int, default=DEFAULT_TILE_SIZE, help="Tile size in pixels")
args = parser.parse_args()

if any(x < 1 for x in (args.width, args.height, args.tile_size)):
    parser.error("All dimensions must be positive integers.")


def main():
    pg.init()

    TILE_FONT = pg.font.SysFont(None, int(args.tile_size*TILE_TEXT_SIZE))
    
    screen = pg.display.set_mode((args.width * args.tile_size, args.height * args.tile_size))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()

    grid = utils.grid.TerrainGrid(args.width, args.height)

    grid_drawer = renderer.gridDrawer.GridDrawer(screen, TILE_FONT, grid, args.tile_size)
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
