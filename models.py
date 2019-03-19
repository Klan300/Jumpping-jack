base_platform_height = 24
base_platform_width = 71
center_character_x = 28
center_character_y = 25
Gravity = -1


class World:
    def __init__(self,width,height):

        self.base_platform = Platform(self,width//2,base_platform_height//2)
        self.character = Character(self,width//2-3,base_platform_height+center_character_y)



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
    





        

        