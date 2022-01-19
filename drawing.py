import random
import pygame as pg
import lib.hex_to_rgb as hex_to_rgb

WHITE = (255, 255, 255)


def main():

    pg.init()
    logo = pg.image.load("lib/logo2.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("minimum program")

    running = True
    while running:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


screen = pg.display.set_mode((800, 800))
screen.fill(WHITE)


class Palette:
    def __init__(self, colors: list):
        self.colors = colors
        self.color_numer = len(colors)

    def get_rand_color(self):
        return self.colors[random.randint(0, self.color_numer - 1)]

    def get_weight_color(self):
        pass

    def get_colors(self):
        return self.colors


night_sky_light = Palette(hex_to_rgb.list(
    "5C1387	6C2B93	7D429F	8D5AAB	9D71B7	AE89C3	BEA1CF	CEB8DB	DED0E7	EFE7F3	FFFFFF".split(
        "	")
))
night_sky_dark = Palette(hex_to_rgb.list(
    "5C1387	53117A	4A0F6C	400D5F	370B51	2E0A44	250836	1C0628	12041B	09020D	000000".split(
        "	")
))


def draw_night_sky(pal: Palette):

    for pixel_col in range(80):
        for pixel_row in range(160):
            pg.draw.rect(screen, pal.get_rand_color(),
                         [pixel_row*5, pixel_col*5, 5, 5])


def draw_night_sky_2(pal: Palette):

    for pixel_col in range(80, 160):
        for pixel_row in range(160):
            pg.draw.rect(screen, pal.get_rand_color(),
                         [pixel_row*5, pixel_col*5, 5, 5])


draw_night_sky(night_sky_light)
draw_night_sky_2(night_sky_dark)
main()
