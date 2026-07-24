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


    def run(self,dt):
        pass
    def get_direction(self):
        pass


