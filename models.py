from random import randint


base_platform_height = 24
base_platform_width = 71
center_character_x = 25 + 3
center_character_y = 25
Gap_platform  = 35
Gravity = -1


class World:
    def __init__(self,width,height):

        self.base_platform = Platform(self,width//2,base_platform_height//2)
        self.character = Character(self,width//2-3,base_platform_height+center_character_y)
        self.platform_list = Platform_list(self)



    
class Platform_list:
    def __init__(self,world):
        self.world = world
        self.platform_now = []


    def create_start_platform(self):
        count = 0
        for y in range(48,750,Gap_platform):
            x = randint(0,500)
            if count > 0:
                if self.platform_now[count-1].x + 300 >= x <= self.platform_now[count-1].x - 300:
                    x = randint(0, 500)
            self.platform_now.append(Platform(self.world,x,y))

        return self.platform_now

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

        self.touch_platform = True





    





        

        
