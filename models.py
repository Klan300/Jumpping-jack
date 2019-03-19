base_platform_height = 24
base_platform_width = 71
character_height = 50
character_widht = 26


class World:
    def __init__(self,width,height):

        self.base_platform = Platform(self,width//2,base_platform_height//2)
        self.character = Character(self,width//2,base_platform_height+character_height//2)



class Platform:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        

class Character:
    def __init__(self, world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.Stop = True
    





        

        