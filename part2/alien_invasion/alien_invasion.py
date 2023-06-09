import sys
from time import sleep

import pygame  # 包含开发游戏所需的功能
import setuptools.config

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

"""游戏主程序"""


class AlienInvasion:
    def __init__(self):
        # 初始化背景设置
        pygame.init()
        # 属性设置，便于同类中用self使用
        self.settings = Settings()

        # 全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # 创建一个显示窗口，一个surface对象(表示整个游戏窗口), surface是屏幕的一部分，用于显示游戏元素，每个元素都是一个surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 尺寸，宽、高
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        # 设置背景色[0,255](红(255,0,0)、绿(0,255,0)、蓝(0,0,255))
        # self.bg_color = (230, 230, 230)  # 浅灰色

        # 编组，用于存储所有有效的子弹
        self.bullets = pygame.sprite.Group()
        # 外星人分组
        self.aliens = pygame.sprite.Group()  # 少写了一个括号，导致下面self.aliens.draw(self.screen)报错,  draw() missing 1 required positional argument: 'surface'
        self._create_fleet()

        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            # print(11111111) 不断执行，一个死循环
            self._check_events()  # 处理按键事件

            if self.stats.game_active:
                self.ship.update()  # 更新飞船位置
                self._update_bullets()  # 更新子弹位置
                self._update_aliens()  # 更新外星人位置

            self._update_screen()  # 依据上面位置重画

    def _check_events(self):
        # 监视键盘和鼠标的事件
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 处理按下键盘
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 处理松开
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # 单机出的元组(x,y)
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.pre_score()
            self.sb.pre_level()
            self.sb.pre_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # 游戏开始，隐藏光标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # 大写Q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  # size是一个元组
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)  # 流出左右两个外星人宽度
        number_aliens_x = available_space_x // (2 * alien_width)  # 整除, 每个外星人宽度+外星人间隔

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        # 垂直可用空间：屏幕高度 - 第一行外星人距离最上面屏幕的距离(1个外星人高度) - 飞船高度 - 外星人群最初与飞船之间的距离(外星人高度的两倍)
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 每行都创建外星人
        for row_number in range(number_rows):
            # 第一行外星人
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 一个外星人宽度作为离屏幕左边间距 + 两个外星人距离(一个间隔) * 第几个外星人
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # 一个外星人 + 外星人之间间隔
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # 按照元素位置，将所有元素绘制到屏幕上
    def _update_screen(self):
        """每次循环都重新画一遍所有元素"""
        # 每次循环时都重填充背景
        self.screen.fill(self.settings.bg_color)
        # 将飞船绘制到屏幕上
        self.ship.blitme()
        # 绘制每个子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 将编组内的所有元素绘制到指定surface上
        self.aliens.draw(self.screen)

        self.sb.show_score()

        # 未开始则显示play按钮, 最后绘制，放到其他东西之上
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()  # 对编组调用update时，其自动对其中的每个sprite调用update，这就调用了bullet.py的update

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中外星人，若是则删除对应的子弹和外星人
        # 返回一个字典，每个键都是一个子弹，关联的值是被该子弹击中的外星人
        # 两个true表明让pygame删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.pre_score()
            self.sb.check_high_score()

        # 没有外星人了，清空子弹，重新创建外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.pre_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        # 更新所有外星人的位置
        self.aliens.update()

        # 检测外星人和飞船碰撞
        if pygame.sprite.spritecollideany(self.ship,
                                          self.aliens):  # 检查group是否有成员与sprite发生碰撞，遍历aliens找到第一个与ship碰撞的外星人，若没有则返回none
            # print("ship hit!!!")
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direct()
                break

    def _change_fleet_direct(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed  # 每个下移
        self.settings.fleet_direction *= -1  # 1或者-1

    def _ship_hit(self):
        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1
            self.sb.pre_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    # 检查是否到达屏幕底端
    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
