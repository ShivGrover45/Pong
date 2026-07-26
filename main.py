from settings import *
from sprites import *



class Game():
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock=pygame.time.Clock()
        self.running=True
        self.all_sprites=pygame.sprite.Group()
        self.paddle_sprites=pygame.sprite.Group()
        self.player=Players((self.paddle_sprites,self.all_sprites))
        self.ball=Ball(self.all_sprites,self.paddle_sprites,(640,360))
        Opponents((self.all_sprites,self.paddle_sprites),self.ball)
        self.score={'player':0,'opponent':0}
        self.font=pygame.font.Font(None,160)


    def run(self):
       
        while self.running:
            dt=self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                #update
            self.all_sprites.update(dt)
                #draw
            self.display_surface.fill(COLORS.get('bg'))
            self.display_score()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.QUIT

    def display_score(self):
        #player score
        player_surf=self.font.render(str(self.score['player']),True,COLORS['bg detail'])
        player_surf_rect=player_surf.get_frect(center=(WINDOW_WIDTH/2+100,WINDOW_HEIGHT/2))
        self.display_surface.blit(player_surf,player_surf_rect)


if __name__=="__main__":
    game=Game()
    game.run()
