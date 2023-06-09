import pygame
from pygame.sprite import Sprite

"""飞船"""


class Ship(Sprite):
    def __init__(self, ai_game):  # ai_game is AlienInvasion
        super().__init__()
        # 设定初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 返回飞船的surface
        self.rect = self.image.get_rect()

        # 放在底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # 绘制飞船到指定位置
        self.screen.blit(self.image, self.rect)

    # 坐标原点为left,top角(0,0)
    def update(self):
        # 根据移动标志调整飞船位置，每次移动一个settings.ship_speed，不能超出窗口大小
        if self.moving_right and self.rect.right < self.screen_rect.right:  # 向右
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  # 向左
            self.x -= self.settings.ship_speed

        # rect只存储整数部分
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
