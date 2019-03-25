from random import randint
import arcade.key


platform_center_y = 12
platform_center_x = 35.5
center_character_x = 25 + 3
center_character_y = 24
Gap_platform  = 35
GRAVITY = -1
MOVEMENT_SPEED = 2

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

        self.base_platform = Platform(self,width//2,platform_center_y)
        self.character = Character(self,width//2-3,platform_center_y+center_character_y)
        self.platform_list = Platform_list(self)


    def update(self,delta):
        self.character.update(delta)


    def on_key_press(self, key, key_modifiers):
        if key in KEY_MAP:
            self.character.direction = KEY_MAP[key]
        
    def on_key_relese(self, key, key_modifiers):
        if key in KEY_MAP:
            self.character.direction = DIR_STILL

    

    
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

    def touch_player(self,character):
        if character.platform_checker:
            Gravity = 0
            character.y += 15
            Gravity = -1
            
    

class Character:
    GRAVITY = -1

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
        self.y -= Character.GRAVITY
    

    def platform_checker(self,platform_list):
        for platform in platform_list:
            if platform.y + platform_center_y == self.y - center_character_y:
                if platform.x - platform_center_x <= self.x + center_character_x <= platform.x + platform_center_x or platform.x - platform_center_x <= self.x - center_character_x <= platform.x + platform_center_x:
                    return True








    





        

        
