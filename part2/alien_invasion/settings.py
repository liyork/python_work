class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 300  # 可调整，子弹变宽了，一次可消灭的外星人多了
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 深灰色
        self.bullets_allowed = 3

        # 外星人

        # 向下速度
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # 随游戏而变化的属性
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0  # 子弹速度
        self.alien_speed = 1.0  # 横向速度

        # 1:向右，-1向左
        self.fleet_direction = 1

        # 每个外星人得分
        self.alien_points = 50

    # 提高速度
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
