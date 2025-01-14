import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.message import draw_message
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.obstacles.cloud import Cloud

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 13
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.running = False
        self.score = 0
        self.high_score = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                pygame.mixer.music.load('dino_runner/assets/Sounds/Intro.mp3')
                pygame.mixer.music.play(20)
                self.show_menu()
                
        pygame.display.quit()
        pygame.quit()
        
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.score = 0
        self.game_speed = 13

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        
    def update_score(self):
        self.score += 1
        
        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((81, 209, 246))
        self.draw_background()
        self.draw_score()
        self.draw_speed()      
        self.draw_death()       
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)  
        self.power_up_manager.draw(self.screen)      
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        

        
    def draw_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        Game.resume(self, f'Score: {self.score} ', 115, 100)    
        Game.resume(self, f'High score: {self.high_score}', 900, 50)

    def draw_speed(self):
        Game.resume(self, f'Speed: {self.game_speed-13}', 100, 50)   
    
    def draw_death(self):
        Game.resume(self, f'Number of deaths: {self.death_count}', 500, 50)  

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/ 1000, 2)
            if time_to_show >= 0:
                draw_message(
                    f'{self.player.type.capitalize()} enable for {time_to_show} seconds',
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=250
                )
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def resume(self, message, width, height):       
        font = pygame.font.FontType(FONT_STYLE, 30)
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)   

    def over(self, message, width, height):      
        font = pygame.font.FontType(FONT_STYLE, 50)
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)  

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

            elif event.type == pygame.KEYDOWN:
                if self.death_count < 4:
                    self.run()
                else: 
                    self.death_count = 0
                    self.run()

    def show_menu(self):
        self.screen.fill((155, 155, 155))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            Game.resume(self,'Press any key to start',  half_screen_width, half_screen_height)
        elif self.death_count > 0 and self.death_count <= 3:
            Game.resume(self,'Press any key to restart', half_screen_width, half_screen_height)   
            Game.resume(self, f'Number of deaths: {self.death_count}', half_screen_width, half_screen_height+100)
            Game.resume(self, f'Speed: {self.game_speed-13}', half_screen_width, half_screen_height+150)
            Game.resume(self, f'Score: {self.score}', half_screen_width, half_screen_height+200)
            Game.resume(self, f'High Score: {self.high_score}', half_screen_width, half_screen_height+250)
            self.screen.blit(ICON, (half_screen_width-20, half_screen_height-140))
        else:
            self.screen.blit(ICON, (half_screen_width-50, half_screen_height+75))
            Game.over(self,'Game Over',  half_screen_width, half_screen_height)
            Game.resume(self, f'High Score: {self.high_score}', half_screen_width, half_screen_height+250)
        
        pygame.display.update()
        self.handle_events_on_menu()