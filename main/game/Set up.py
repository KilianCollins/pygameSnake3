import pygame as pg
import sys
import random

class SetUp(object):
    """does the boilerplate for you in pygame basic set up"""
    pg.init()
    # pg.font.init() automatically called by pg.init()

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    Clock = pg.tick(60)

    def screen(self, sw=SCREEN_WIDTH, sh=SCREEN_HEIGHT, caption="game_screen", ):
        pg.display.set_mode((sw, sh))
        pg.display.set_caption(caption)

    def game_loop(self, run=True,):
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            pg.display.update()
            self.Clock.tick(10)


    def __init__(self):
        self.Clock.tick(10)


