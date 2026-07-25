from settings import *
from random import choice,uniform
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
        self.image=pygame.surface.Surface(SIZE['ball'],pygame.SRCALPHA)
        pygame.draw.circle(self.image,COLORS['ball'],(10,10),10)
        self.rect=self.image.get_frect(center=pos)
        self.direction=pygame.Vector2(choice((1,-1)),uniform(0.7,0.8)*choice((1,-1)))
        self.speed=SPEED['ball']
    def move(self,dt):
        self.rect.center+=self.direction*self.speed*dt
    def wall_collision(self):
        if self.rect.top<0:
            self.rect.top=0
            self.direction.y=-1
        if self.rect.bottom>WINDOW_HEIGHT:
            self.rect.bottom=WINDOW_HEIGHT
            self.direction.y=1
    def update(self,dt):
        self.move(dt)
        self.wall_collision()


