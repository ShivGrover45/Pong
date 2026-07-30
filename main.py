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
        self.ball=Ball(self.all_sprites,self.paddle_sprites,(640,360),self.update_score)
        Opponents((self.all_sprites,self.paddle_sprites),self.ball)
        self.score={'player':0,'opponent':0}
        self.font=pygame.font.Font(None,160)
        try:
            with open(join('../data','scores.txt')) as score_file:
                json.load(score_file)
        except:
            self.score={'player':0,'opponent':0}


    def run(self):
       
        while self.running:
            dt=self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            with open(join('../data','scores.txt'),'w') as score_file:
                json.dump(self.score,score_file)
                
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

        #Opponenent Score
        opponent_surf=self.font.render(str(self.score['opponent']),True,COLORS['bg detail'])
        opponent_surf_rect=opponent_surf.get_frect(center=(WINDOW_WIDTH/2-100,WINDOW_HEIGHT/2))
        self.display_surface.blit(opponent_surf,opponent_surf_rect)

        #Line Seperator
        pygame.draw.line(self.display_surface,COLORS['bg detail'],(WINDOW_WIDTH/2,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT),3)
    def update_score(self,side):
        self.score['player' if side=='player' else 'opponent']+=1
        if self.score[side]==5:
            self.result_screen(side)
    def result_screen(self,side):
        if side=='opponent':
            pass
        elif side=='player':
            pass


if __name__=="__main__":
    game=Game()
    game.run()
