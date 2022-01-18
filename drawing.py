import os
import pygame as pg


main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

backdrop = pg.display.set_mode(size=(800, 600))

