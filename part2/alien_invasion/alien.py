import pygame
from pygame.sprite import Sprite

"""外星人"""


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人的矩形x, y
        # 最初在左上角附近
        self.rect.x = self.rect.width  # 将矩形左边距设置为矩形宽度
        self.rect.y = self.rect.height

        # 用于带有float类型的计算
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True

    def update(self):
        # 向左或右移动
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)  # 外星人准确位置，可存储小数
        self.rect.x = self.x
