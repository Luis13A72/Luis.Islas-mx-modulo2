import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE 
from dino_runner.components.dinosaur import Dinosaur #se importa nuestra clase
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)   #Muestra el titulo que se presenta
        pygame.display.set_icon(ICON)       #Coloca una imagen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    #Define el tamaño de la pantalla del juego
        self.clock = pygame.time.Clock()    #Define los tiempos del juego
        self.playing = False    
        self.game_speed = 7    #20 posiciones que se irán cambiando
        self.x_pos_bg = 0       #pocision en X
        self.y_pos_bg = 380     #posición en Y
        self.player = Dinosaur() #/Es la instancia de la clase Dinosaur
        self.obstacle_manager = ObstacleManager()
        self.running = False
        self.score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit() 


    def run(self):
        self.obstacle_manager.reset_obstacles()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():    #Lista de eventos del teclado
            if event.type == pygame.QUIT:   #La funcion del tache para cerrar la ventana
                self.playing = False        #Saca del juego

            
                
                
    def update(self):

        self.update_score()
        user_input = pygame.key.get_pressed()    #Todos los que se han presionado
        self.player.update(user_input)    #/Llama al metodo que está en la clase de la instancia
        self.obstacle_manager.update(self)

    def update_score(self):

        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 0.5


    def draw(self):
        self.clock.tick(FPS)        #El tick dice en cada segundo cuantos frames se actualizan
        self.screen.fill((255, 255, 255))   #Color que se pintará la pantalla  
        self.draw_background()      #llama al metodo del fondo de pantalla
        self.draw_score()
        self.player.draw(self.screen)          #/Pasa los datos del screen, para dibujar al dinosaur
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()   #Actualiza todos los objetos
        
        

    def draw_background(self):
        image_width = BG.get_width()    #El ancho de la imagen del fondo
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))    #El Blit es para avisarle que se pondra un objeto en pantalla, para después mostrar 
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg)) #BG: imagen  y luego las coordenadas
        if self.x_pos_bg <= -image_width:       #Cuando llegué al limite creará otra imagen
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed    #Disminuira a la velocidad que se le haya colocado

    def draw_score(self):
        font = pygame.font.FontType(FONT_STYLE, 30)
        text = font.render(f'score: {self.score}', True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect) 

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

             
    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height =SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render('Press any key to start', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        else:
            pass

        self.screen.blit(ICON, (half_screen_width -20, half_screen_height - 140))
        pygame.display.update()
        self.handle_events_on_menu()