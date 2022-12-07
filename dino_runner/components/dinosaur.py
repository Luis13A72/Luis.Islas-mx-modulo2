import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING #Se importa la constante a usar
class Dinosaur:
    def __init__(self): #Siempre ddebe estar para cuando se agregue un objeto al juego
        self.image = RUNNING[0] #Al ser una lista inicia en posicion 0
        self.dino_rect = self.image.get_rect()   #Coordenadas que tendra nuestra imagen, dando todos su parametros
        self.dino_rect.x =80    #Dibujar donde se imprime el dinosaurio
        self.dino_rect.y =310   #Dibujar donde se imprime el dinosaurio
        self.step_index = 0    #Atributo de los pasos del dinosaurio

        self.dino_run = True     #//Se crean dos variables mas
        self.dino_jump = False   #//Se crean dos variables mas
        self.jump_vel = 8.5 #//Se creala variable de velocidad de salto

        self.image = DUCKING[0] #
        self.dino_duck = False

        self.duck_time = 0.5  

    def update(self, user_input):   #Siempre ddebe estar para cuando se agregue un objeto al juego

        if self.dino_run:
            self.run()  #Si está en Run se manda a llamar al metodo run
        elif self.dino_jump:
            self.jump() #Si está en Run se manda a llamar al metodo jump
        elif self.dino_duck:
            self.duck()
        
            
        if user_input[pygame.K_UP] and not self.dino_jump: #Entrada del usuario por medio de pygame para el comando arriba
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
       
        elif user_input[pygame.K_DOWN] and not self.dino_duck and not self.dino_jump:
            
            self.dino_duck = True
            self.dino_run = False 
            self.dino_jump = False
        
        elif not self.dino_jump and not self.dino_duck:    #Si no está saltando entonces está corriendo
            self.dino_jump = False
            self.dino_duck = False
            self.dino_run = True
            
            
        if self.step_index >= 10: #se debe resetear los steps para reiniciar la animación
            self.step_index = 0  

        


    def jump(self):
        self.image = JUMPING    
        self.dino_rect.y -= self.jump_vel*4
        self.jump_vel -= 0.8

        if self.jump_vel < -8.5:
            self.dino_rect.y = 310
            self.dino_jump = False
            self.jump_vel = 8.5

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]  #Operación ternaria, operación que pone un If y un Else, en una sola linea
        self.dino_rect.x =80    #Dibujar donde se imprime el dinosaurio
        self.dino_rect.y =310   #Dibujar donde se imprime el dinosaurio
        self.step_index += 1   #Los Step avanzaran de uno en uno hasta llegar  a 5        
        

    def duck(self):    

        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]  #Operación ternaria, operación que pone un If y un Else, en una sola linea
        self.dino_rect.x =80    #Dibujar donde se imprime el dinosaurio
        self.dino_rect.y =350   #Dibujar donde se imprime el dinosaurio
        self.step_index += 1   #Los Step avanzaran de unoen uno hasta llegar  a 5 
        self.duck_time -= 0.8
        
        if self.duck_time < -0.5:
            self.dino_duck = False
            self.duck_time = 0.5   


    def draw(self, screen):     #Siempre debe estar para cuando se agregue un objeto al juego, donde lo dibujara
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y)) # Se le pasa la imagen y la ubicación