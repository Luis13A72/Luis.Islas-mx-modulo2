import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_big import CactusBig
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing = False
                break

        if len(self.obstacles) == 0:
            self.obstacles.append(CactusBig(LARGE_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing = False
                break            

        if len(self.obstacles) == 0:
            self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing = False
                game.death_count += 1
                break  

            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []