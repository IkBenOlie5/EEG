import os
from pathlib import Path

import constants as c
import pygame as pg

game_directory = Path(os.path.dirname(__file__))
assets_directory = os.path.join(game_directory, c.ASSETS_FOLDER)


def load_png(filename):
    image = pg.image.load(os.path.join(assets_directory, filename))

    if image.get_alpha() is None:
        image = image.convert()
        return image
    image = image.convert_alpha()
    return image
