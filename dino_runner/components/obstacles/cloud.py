import random, pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH, SCREEN_HEIGHT, BG

class Cloud():
    def __init__(self, image):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos = 0
        self.y_pos = 0

    def cloud_background (self):
        self.x_pos = 1000
        self.y_pos = 300
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos, self.y_pos))
        self.screen.blit(CLOUD, (image_width + self.x_pos, self.y_pos))
        if self.x_pos <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos, self.y_pos))
            self.x_pos = 0
        self.x_pos -= self.game_speed