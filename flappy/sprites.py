import random

import numpy as np
import pygame as pg

import constants as c


class Background(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = game.background_image.copy()
        self.rect = self.image.get_rect()


class Bird(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__((game.all_sprites,))
        self.game = game
        self.image = game.bird_image.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.vel = 0
        self.y = y

    def detect_jump(self):
        try:
            to_read = int(c.SAMPLERATE / self.game.fps)
        except ZeroDivisionError:  # when the game starts up, fps = 0
            return False
        data = self.game.stream.read(to_read)[0].flatten()
        return np.min(data) < -c.THRESHOLD or np.max(data) > c.THRESHOLD

    def update(self):
        if self.detect_jump():
            self.vel = c.JUMP_SPEED

        if self.vel < c.FALL_MAX:
            self.vel += c.FALL_ACCEL

        self.y += self.vel * self.game.dt
        self.rect.centery = self.y

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= c.HEIGHT:
            self.rect.bottom = c.HEIGHT

        for pipe in self.game.pipes:
            if self.rect.colliderect(pipe.rect) and (
                self.y > pipe.y or self.y < pipe.y - c.BETWEEN_PIPES
            ):
                pipe.kill()
                self.y = c.START_Y


class Pipe(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__((game.all_sprites, game.pipes))
        self.game = game
        self.image = pg.surface.Surface(
            (game.pipe_image.get_width(), c.HEIGHT), pg.SRCALPHA
        )
        self.rect = self.image.get_rect()
        self.y = random.randint(c.BETWEEN_PIPES, c.HEIGHT)

        self.image.blit(game.pipe_image, (0, self.y))
        self.image.blit(
            pg.transform.flip(game.pipe_image, flip_x=False, flip_y=True),
            (0, self.y - c.BETWEEN_PIPES - game.pipe_image.get_height()),
        )

        self.rect.x = c.WIDTH

    def update(self):
        self.rect.x -= c.PIPE_SPEED * self.game.dt

        if self.rect.right < 0:
            self.kill()
