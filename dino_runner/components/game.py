import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur #se importa nuestra clase

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)   #Muestra el titulo que se presenta
        pygame.display.set_icon(ICON)       #Coloca una imagen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    #Define el tamaño de la pantalla del juego
        self.clock = pygame.time.Clock()    #Define los tiempos del juego
        self.playing = False    
        self.game_speed = 20    #20 posiciones que se irán cambiando
        self.x_pos_bg = 0       #pocision en X
        self.y_pos_bg = 380     #posición en Y

        self.player = Dinosaur() #/Es la instancia de la clase Dinosaur

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():    #Lista de eventos del teclado
            if event.type == pygame.QUIT:   #La funcion del tache para cerrar la ventana
                self.playing = False        #Saca del juego

            
                
                
    def update(self):
        user_input = pygame.key.get_pressed()    #Todos los que se han presionado
        self.player.update(user_input)    #/Llama al metodo que está en la clase de la instancia

    def draw(self):
        self.clock.tick(FPS)        #El tick dice en cada segundo cuantos frames se actualizan
        self.screen.fill((255, 255, 255))   #Color que se pintará la pantalla  
        self.draw_background()      #llama al metodo del fondo de pantalla
        self.player.draw(self.screen)          #/Pasa los datos del screen, para dibujar al dinosaur
        pygame.display.update()     #Actualiza un objeto en particular
        pygame.display.flip()   #Actualiza todos los objetos

    def draw_background(self):
        image_width = BG.get_width()    #El ancho de la imagen del fondo
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))    #El Blit es para avisarle que se pondra un objeto en pantalla, para después mostrar 
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) #BG: imagen  y luego las coordenadas
        if self.x_pos_bg <= -image_width:       #Cuando llegué al limite creará otra imagen
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed    #Disminuira a la velocidad que se le haya colocado
