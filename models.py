from random import randint
import arcade
from coldetect import check_player_platform_collsion , check_time
import time
import sys


platform_center_y = 12
platform_center_x = 35.5
center_character_x = 25 + 3
center_character_y = 24
Gap_platform  = 30
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750



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
    GRAVITY = 5

    def __init__(self,width,height):

        self.character = Character(self,width//2-3,platform_center_y*2+center_character_y)
        self.platform_now = Platform_list(self)

    def update(self,delta):
        if self.platform_now.platform_checker(self.character):
            self.GRAVITY = 0
            self.platform_now.move_platform(self.character)
        else:
            self.character.y -= self.GRAVITY
            self.GRAVITY = 5
            self.platform_now.move_platform(self.character)
        self.out_from_screen()
        self.platform_manage()
        self.character.update(delta)
        if self.character.y-23 <= 0:
            self.game_end()
    

    def on_key_press(self, key, key_modifiers):
        if key in KEY_MAP:
            if key == arcade.key.SPACE :
                if self.COUNT_UP <= 2:
                    self.character.direction = KEY_MAP[key]
                    self.COUNT_UP += 1
                else:
                    if self.platform_now.platform_checker(self.character):
                        self.COUNT_UP -= 2
            else:
                self.character.direction = KEY_MAP[key]       


    def out_from_screen(self):
        if self.character.x >= SCREEN_WIDTH:
            self.character.x = 0 
        elif self.character.x <= 0:
            self.character.x = SCREEN_WIDTH
        
        
    def game_end(self):
        start = time.time()
        self.character.direction = DIR_STILL
        while True:
            end = time.time()
            if end - start >= 3:
                sys.exit()
                break
        



    def on_key_relese(self, key, key_modifiers):
        if key in KEY_MAP:
            self.character.direction = DIR_STILL

    def platform_manage(self):
        self.platform_now.delete_platform()
        self.platform_now.add_platform()

    
class Platform_list:
    def __init__(self,world):
        self.world = world
        self.base_platform = Platform(self, SCREEN_WIDTH//2, platform_center_y)
        self.platform_now = [self.base_platform]

    def create_start_platform(self):
        count = 0
        for y in range(48,750,Gap_platform):
            x = randint(0,500)
            if count > 0:
                while self.platform_now[count-1].x + 300 >= x <= self.platform_now[count-1].x - 300:
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


    def plate_form_creater(self):
        x = randint(0, 500)
        y = 500
        self.platform_now.append(Platform(self.world, x, y))


    def move_platform(self,character):
        if character.y >= SCREEN_HEIGHT/2:
            move = character.y - SCREEN_WIDTH/2
            for platform in self.platform_now:
                platform.y -= move/35  
        

    def delete_platform(self):
        count = 0
        for i in range(len(self.platform_now)):
            if self.platform_now[i-count].y <= 0:
                self.platform_now.pop(i-count)
                count += 1
        

    def add_platform(self):
        count = 0
        if self.platform_now[-1].y >= 30:
            for y in range(int((self.platform_now[-1].y + 30)//1),SCREEN_HEIGHT,Gap_platform):
                x = randint(0, 500)
                if count > 0:
                    while self.platform_now[count-1].x + 300 >= x <= self.platform_now[count-1].x - 300:
                        x = randint(0, 500)
                self.platform_now.append(Platform(self.world, x, y))
                count += 1




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



                    








    





        

        
