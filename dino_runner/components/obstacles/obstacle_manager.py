import pygame, random
from dino_runner.utils.constants import SMALL_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def crash(self,game):
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                game.death_count +=1
                break        
        return  

    def update (self, game):
        decision = random.randint(0,1)
        if decision == 0:
            if len(self.obstacles) == 0:
                cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'BIG'
                cactus = Cactus(cactus_type)
                self.obstacles.append(cactus)
            ObstacleManager.crash(self, game)
        else:
            if len(self.obstacles) == 0:
                self.obstacles.append(Bird(BIRD))
            ObstacleManager.crash(self, game)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        
        self.obstacles = []

      