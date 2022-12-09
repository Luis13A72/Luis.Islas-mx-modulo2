import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.wings = 0
        super().__init__(image, self.type) #super invoca al constructor del obbstaculo
        self.rect.y = random.randint(225,325)

    def draw(self, SCREEN):
        if self.wings >=9:
            self.wings = 0
        SCREEN.blit(self.image[self.wings//5],self.rect)
        self.wings +=1