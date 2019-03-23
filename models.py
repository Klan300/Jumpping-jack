from random import randint
import arcade.key


base_platform_height = 24
base_platform_width = 71
center_character_x = 25 + 3
center_character_y = 25
Gap_platform  = 35
Gravity = -1
MOVEMENT_SPEED = 4

DIR_STILL = 0
DIR_RIGHT = 1
DIR_LEFT = 2

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_RIGHT: (1, 0),
               DIR_LEFT: (-1, 0)}

KEY_MAP = {arcade.key.LEFT: DIR_LEFT,
           arcade.key.RIGHT: DIR_RIGHT}

class World:
    def __init__(self,width,height):

        self.base_platform = Platform(self,width//2,base_platform_height//2)
        self.character = Character(self,width//2-3,base_platform_height+center_character_y)
        self.platform_list = Platform_list(self)


    def update(self,delta):
        self.character.update(delta)


    def on_key_press(self, key, key_modifiers):
        if key in KEY_MAP:
            self.character.direction = KEY_MAP[key]

    

    
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
            count += 1

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
        self.direction = DIR_STILL    
        self.touch_platform = True


    def update(self, delta):
        self.move(self.direction)

    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]
    





    





        

        
