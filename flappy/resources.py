import os
from pathlib import Path

import pygame as pg

import constants as c

game_directory = Path(os.path.dirname(__file__))
assets_directory = os.path.join(game_directory, c.ASSETS_FOLDER)
images_directory = os.path.join(assets_directory, "images")
sounds_directory = os.path.join(assets_directory, "sounds")
fonts_directory = os.path.join(assets_directory, "fonts")


def load_png(filename):
    image = pg.image.load(os.path.join(images_directory, filename))

    if image.get_alpha() is None:
        image = image.convert()
        return image
    image = image.convert_alpha()
    return image


def load_sound(filename):
    return pg.mixer.Sound(os.path.join(sounds_directory, filename))


def load_font(filename, size):
    return pg.font.Font(os.path.join(fonts_directory, filename), size)
