class World:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

    def run(self, events):
        self.display.fill((10, 200, 60))
