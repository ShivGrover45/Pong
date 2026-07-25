from settings import *

class Players(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        #image 
        self.image=pygame.Surface(SIZE['paddle'])
        self.image.fill(COLORS['paddle'])


        #rect
        self.rect=self.image.get_frect(center=POS['player'])
        self.direction=0
        self.speed=SPEED.get('player')


    def run(self,dt):
        self.rect.centery+=self.direction*self.speed*dt
        self.rect.top=0 if self.rect.top<0 else self.rect.top
        self.rect.bottom=WINDOW_HEIGHT if self.rect.bottom>WINDOW_HEIGHT else self.rect.bottom
    def get_direction(self):
        keys=pygame.key.get_pressed()
        self.direction=int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
    def update(self,dt):
        self.get_direction()
        self.run(dt)
        
class Ball(pygame.sprite.Sprite):
    def __init__(self,groups,paddle_sprites,pos):
        super().__init__(groups)
        self.image=pygame.surface.Surface(SIZE['ball'])
        self.image.fill(COLORS['ball'])
        self.rect=self.image.get_frect(center=pos)


