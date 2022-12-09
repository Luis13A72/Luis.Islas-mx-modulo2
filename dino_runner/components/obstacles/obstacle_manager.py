import pygame, random
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, SHIELD_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.sound_crash = pygame.mixer.Sound('dino_runner/assets/Sounds/Crash.mp3')

    def update (self, game):
        decision = random.randint(0,1)      
        if decision == 0:
            if len(self.obstacles) == 0:
                cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'     
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

    def crash(self,game):       ###
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    pygame.time.delay(1000)
                    self.sound_crash.play()
                    game.playing = False
                    game.death_count +=1
                    break  
                else:
                    self.obstacles.remove(obstacle)    
  
    def reset_obstacles(self):  
        self.obstacles = []