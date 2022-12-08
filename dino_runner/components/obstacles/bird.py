import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type) #super invoca al constructor del obbstaculo
        self.rect.y = random.randint(225,325)

    def fly(self):
        self.type = BIRD[0] if self.step_index < 5 else BIRD[1]  #Operación ternaria, operación que pone un If y un Else, en una sola linea
        self.dino_rect.y =310   #Dibujar donde se imprime el dinosaurio
        self.step_index += 1   #Los Step avanzaran de uno en uno hasta llegar  a 5  