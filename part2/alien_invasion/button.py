import pygame.font  # 能将文本渲染到屏幕上

""""按钮"""


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 按钮属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 亮绿色
        self.text_color = (255, 255, 255)  # 白色
        self.font = pygame.font.SysFont(None, 48)  # none默认字体，48字号

        # 矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._pre_msg(msg)

    def _pre_msg(self, msg):
        # 将msg渲染为图像
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)  # Truetrue表明开启反锯齿功能, 文本颜色，背景色
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #  绘制按钮
        self.screen.fill(self.button_color, self.rect)
        #  绘制文本
        self.screen.blit(self.msg_image, self.msg_image_rect)
