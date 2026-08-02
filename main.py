from settings import *
from sprites import *



class Game():
    def __init__(self):
        pygame.init()
        #game mode 
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")

        self.clock=pygame.time.Clock()
        self.running=True
        #grouping sprites 
        self.all_sprites=pygame.sprite.Group()
        self.paddle_sprites=pygame.sprite.Group()
        self.player=Players((self.paddle_sprites,self.all_sprites))
        self.ball=Ball(self.all_sprites,self.paddle_sprites,(640,360),self.update_score)
        Opponents((self.all_sprites,self.paddle_sprites),self.ball)
        #Player and opponents score
        self.score={'player':0,'opponent':0}
        self.font=pygame.font.Font(None,160)
        self.state='menu'
        #Font for different screens like Main menu Result Screen and Pause Menu
        self.title_font=pygame.font.Font(None,80)
        self.menu_font=pygame.font.Font(None,40)
        self.result_font=pygame.font.Font(None,80)
        self.score_font=pygame.font.Font(None,60)
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

            #drawing main menu for the game
            if self.state=='menu':
                self.main_menu()
                #update
            elif self.state=='playing':
                  self.all_sprites.update(dt)
                #draw
                  self.display_surface.fill(COLORS.get('bg'))
                  self.display_score()
                  self.all_sprites.draw(self.display_surface)
            elif self.state=='game-over':
                self.result_screen()
            pygame.display.update()
        pygame.QUIT
    def main_menu(self):
        if self.state=='menu':
            #displaying title of the game
            self.display_surface.fill(COLORS['bg'])
            title=self.title_font.render("PONG",True,COLORS['paddle'])
            title_rect=title.get_frect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//4))
            #Menu options for the game
            play_game=self.menu_font.render("Press Space to start",True,COLORS['menu title'])
            play_game_rect=play_game.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2))
            esc_game=self.menu_font.render("Press ESC to quit",True,COLORS['menu title'])
            esc_game_rect=esc_game.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+60))
            self.display_surface.blit(title,title_rect)
            self.display_surface.blit(play_game, play_game_rect)
            self.display_surface.blit(esc_game, esc_game_rect)
            keys=pygame.key.get_just_pressed()
            if keys[pygame.K_SPACE]:
                self.state='playing'
            elif keys[pygame.K_ESCAPE]:
                self.running=False
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
            self.winner=side
            self.state='game-over'
    def result_screen(self):
        keys=pygame.key.get_just_pressed()
        if self.winner=='opponent':
            result=self.result_font.render("You Lost! Asshole",True,COLORS['menu title'])
            result_rect=result.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//4))
            label=self.menu_font.render('Final Score',True,COLORS['menu title'])
            label_rect=label.get_frect(center=(WINDOW_WIDTH//2, 300))
            score=self.score_font.render(f"{self.score['opponent']}-{self.score['player']}",True,COLORS['menu title'])
            score_rect=score.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2))
            continuation=self.menu_font.render('Press Space Bar to play again',True,COLORS.get('menu title'))
            continuation_rect=continuation.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+40))
            escape=self.menu_font.render('Press ESC to escape to Main Menu',True,COLORS['menu title'])
            escape_rect=escape.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+100))
            if keys[pygame.K_SPACE]:
                self.reset_game()
                self.state='playing'
            elif keys[pygame.K_ESCAPE]:
                self.state='menu'
            self.display_surface.fill(COLORS["bg"])

            self.display_surface.blit(result, result_rect)
            self.display_surface.blit(label, label_rect)
            self.display_surface.blit(score, score_rect)
            self.display_surface.blit(continuation,continuation_rect)
            self.display_surface.blit(escape,escape_rect)
        elif self.winner=='player':
            
                    result=self.result_font.render("You Won!",True,COLORS['menu title'])
                    result_rect=result.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//4))
                    label=self.menu_font.render('Final Score',True,COLORS['menu title'])
                    label_rect=label.get_frect(center=(WINDOW_WIDTH//2, 300))
                    score=self.score_font.render(f"{self.score['Player']}-{self.score['opponent']}",True,COLORS['menu title'])
                    score_rect=score.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2))
                    continuation=self.menu_font.render('Press Space Bar to play again',True,COLORS.get('menu title'))
                    continuation_rect=continuation.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+40))
                    escape=self.menu_font.render('Press ESC to escape to Main Menu',True,COLORS['menu title'])
                    escape_rect=escape.get_frect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+100))
                    if keys[pygame.K_SPACE]:
                            self.reset_game()
                            self.state='playing'
                    elif keys[pygame.K_ESCAPE]:
                            self.state='menu'
                    self.display_surface.fill(COLORS["bg"])
            
                    self.display_surface.blit(result, result_rect)
                    self.display_surface.blit(label, label_rect)
                    self.display_surface.blit(score, score_rect)
                    self.display_surface.blit(continuation,continuation_rect)
                    self.display_surface.blit(escape,escape_rect)
            


if __name__=="__main__":
    game=Game()
    game.run()
