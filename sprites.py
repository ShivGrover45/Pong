from settings import *

class Players(pygame.sprite.Sprite):
    def __init__(self,groups,x_pos):
        super().__init__(groups)
        #image 
        self.image=pygame.surface.Surface(SIZE['paddle'])


        #rect
        self.rect=self.image.get_frect(center=(x_pos,WINDOW_HEIGHT/2))
        self.direction=pygame.Vector2()
        self.speed=SPEED['player']


