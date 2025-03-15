import pygame
import sys

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ON_FULLSCREEN
from scenes.world import World


class Game:
    def __init__(self):
        self.game_state_manager = GameStateManager("World")

        pygame.init()

        if ON_FULLSCREEN:
            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.world = World(self.display, self.game_state_manager)

        self.states = {"World": self.world}
        
        pygame.display.set_caption("Prodos: New Day")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.states[self.game_state_manager.get_state()].run(events)

            pygame.display.update()
            self.clock.tick(FPS)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game = Game()
    game.run()
