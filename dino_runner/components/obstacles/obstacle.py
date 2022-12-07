import pygame
from pygame.sprite import Sprite #Heredar de la clase el sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect() #Get rec manda a llamar las medidas
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed #Para desplazar el obstaculo y luego desaparecerá
        if self.rect.x < -self.rect.width:
            obstacles.pop()     #Se debe pasar como parametro en el argumento  de update

    def draw(self, screen):     #Siempre recibe el screen, porque se necesita el "lienzo" donde dibujará  
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y)) #Recibe una imagen y la posición donde se colocará la imagen, lo pone pero no lo dibuja


