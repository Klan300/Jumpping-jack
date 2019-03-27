from random import randint
import arcade
from coldetect import check_player_platform_collsion

platform_center_y = 12
platform_center_x = 35.5
center_character_x = 25 + 3
center_character_y = 24
Gap_platform  = 35

MOVEMENT_SPEED = 5
DIR_STILL = 0
DIR_RIGHT = 1
DIR_LEFT = 2
DIR_UP = 3

DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_RIGHT: (1, 0),
               DIR_LEFT: (-1, 0),
               DIR_UP: (0,4)}

KEY_MAP = {arcade.key.LEFT: DIR_LEFT,
           arcade.key.RIGHT: DIR_RIGHT,
           arcade.key.SPACE: DIR_UP}

class World:
    COUNT_UP = 0
    GRAVITY = 4

    def __init__(self,width,height):

        self.base_platform = Platform(self,width//2,platform_center_y)
        self.character = Character(self,width//2-3,platform_center_y*2+center_character_y)
        self.platform_list = Platform_list(self)

    def update(self,delta):
        self.character.update(delta)

        if check_player_platform_collsion(self.character.x, self.character.y, self.base_platform.x, self.base_platform.y):
            self.GRAVITY = 0
        elif self.platform_list.platform_checker(self.character):
            self.GRAVITY = 0
        else:
            self.character.y -= self.GRAVITY
            self.GRAVITY = 4

        

    def on_key_press(self, key, key_modifiers):
        if key in KEY_MAP:
            if key == arcade.key.SPACE :
                if self.COUNT_UP <= 2:
                    self.character.direction = KEY_MAP[key]
                    self.COUNT_UP += 1
                else:
                    if check_player_platform_collsion(self.character.x, self.character.y, self.base_platform.x, self.base_platform.y) or self.platform_list.platform_checker(self.character):
                        self.COUNT_UP -= 2
            else:
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

    def platform_checker(self,character):
        for platform in self.platform_now :
            if check_player_platform_collsion(character.x, character.y, platform.x, platform.y) == True:
                return True
        else:
            return False


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


    def update(self, delta):
        self.move(self.direction)


    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]



                    








    





        

        
