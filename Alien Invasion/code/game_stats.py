class GameStats():
    """Отслеживает статистики для игры Alien Ivasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбравсываться
        self.high_score = 0


    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходу игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1