class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        # 剩余飞船
        self.ships_left = self.settings.ship_limit

        self.score = 0
        self.level = 1
