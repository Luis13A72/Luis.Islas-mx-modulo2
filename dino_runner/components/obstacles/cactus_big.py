import random
from dino_runner.components.obstacles.obstacle import Obstacle

class CactusBig(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type) #super invoca al constructor del obbstaculo
        self.rect.y = 300
    
    

