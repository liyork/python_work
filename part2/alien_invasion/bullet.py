import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 通过使用sprite，可将游戏中相关的元素编组，进而同时操作编组中的所有元素
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # (0,0)除创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)  # 提供left,top位置
        # 从飞船位置来
        self.rect.midtop = ai_game.ship.rect.midtop
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        # 更新位置，每次移动一个self.settings.bullet_speed，不断向上，而x不变
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
