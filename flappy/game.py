import sys

import pygame as pg
import sounddevice as sd

import constants as c
from resources import load_font, load_png, load_sound
from sprites import Background, Bird, Pipe, Score


class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.init()
        self.screen = pg.display.set_mode(c.SIZE, pg.DOUBLEBUF)
        pg.display.set_caption(c.TITLE)
        pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])
        self.clock = pg.time.Clock()

        self.background_image = load_png(c.BACKGROUND_FILE)
        self.bird_image = load_png(c.BIRD_FILE)
        self.pipe_image = load_png(c.PIPE_FILE)

        self.jump_sound = load_sound(c.JUMP_FILE)
        self.die_sound = load_sound(c.DIE_FILE)

        self.score_font = load_font(c.FONT_FILE, c.FONT_SIZE)

        self.score_num = 0

        self.stream = sd.InputStream(samplerate=c.SAMPLERATE, device=c.DEVICE)

        self.dt = 0
        self.t = 0
        self.fps = c.FPS
        self.playing = False

    def new(self):
        self.stream.start()
        self.all_sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()

        self.background = Background(self)
        self.score = Score(self, int(c.WIDTH / 2), c.FONT_Y)
        self.bird = Bird(self, int(c.WIDTH / 2), c.START_Y)

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        if self.t > c.TIME_BETWEEN_PIPES:
            self.t = 0
            Pipe(self)
            self.score_num += 1

        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.background.image, self.background.rect)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.rect)
        pg.display.update()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(c.FPS) / 1000
            self.fps = self.clock.get_fps()
            self.t += self.dt

            try:
                self.dt = 1 / self.fps
            except ZeroDivisionError:
                pass
            pg.display.set_caption(f"{c.TITLE} - FPS: {self.fps:.2f}")

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
