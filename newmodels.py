from random import randint
import arcade
from coldetect import check_player_platform_collsion, check_time
import time
import sys

platform_center_y = 12
platform_center_x = 35.5
center_character_x = 25 + 3
center_character_y = 24
Gap_platform = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850
MOVEMENT_SPEED = 5
GRAVITY = 0.5

DIR_STILL = 0
DIR_RIGHT = 1
DIR_LEFT = 2
DIR_UP = 3

COUNT_UP = 0
DIR_OFFSETS = {DIR_STILL: (0, 0),
               DIR_RIGHT: (1, 0),
               DIR_LEFT: (-1, 0)}

KEY_MAP = {arcade.key.LEFT: DIR_LEFT,
           arcade.key.RIGHT: DIR_RIGHT}


class World:
    COUNT_UP = 0
    STATE_FROZEN = 1
    STATE_STARTED = 2
    STATE_DEAD = 3


    def __init__(self, width, height):

        self.character = Player(
            self, width//2, height//2-300)
        self.platform_now = Platform_list(self)
        self.state = World.STATE_STARTED
        self.score = 0
        self.score_past = 0

    def update(self, delta):
        if self.state in [World.STATE_FROZEN, World.STATE_DEAD]:
            return

        if self.character.vy <= 0:
            if self.platform_now.platform_checker(self.character):
                self.character.jump()
    
        move = self.platform_now.move_platform(self.character)
        self.platform_manage()
        self.score += move
        self.character.update(delta)

        


        if self.character.y-23 <= 0:
            self.character.vy = 0 

        

    def on_key_press(self, key, key_modifiers): 
        if key in KEY_MAP:
            self.character.direction = KEY_MAP[key]



    def on_key_relese(self, key, key_modifiers):
        if key in KEY_MAP:
            self.character.direction = DIR_STILL

    def platform_manage(self):
        self.platform_now.delete_platform()
        self.platform_now.add_platform()



    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    def die(self):
        self.state = World.STATE_DEAD

    def is_dead(self):
        return self.state == World.STATE_DEAD


class Player:
    STATE_FROZEN = 1
    STATE_STARTED = 2
    STARTING_VELOCITY = 0
    JUMPING_VELOCITY = 12

    def __init__(self, world, x, y):
        self.world = world
        self.gravity = GRAVITY
        self.x = x
        self.y = y
        self.py = 0
        self.vy = Player.STARTING_VELOCITY
        self.direction = DIR_STILL
        self.score = 0

    def update(self, delta):
        self.py = self.y
        self.y += self.vy
        self.vy -= self.gravity
        self.move(self.direction)
        self.out_from_screen()


    def out_from_screen(self):
        if self.x >= SCREEN_WIDTH:
            self.x = 0
        elif self.x <= 0:
            self.x = SCREEN_WIDTH


    def jump(self):
        self.vy = Player.JUMPING_VELOCITY

    def move(self, direction):
        self.x += MOVEMENT_SPEED * DIR_OFFSETS[direction][0]
        self.y += MOVEMENT_SPEED * DIR_OFFSETS[direction][1]

class Platform_list:
    def __init__(self,world):
        self.world = world
        self.base_platform = Platform(self, SCREEN_WIDTH//2, platform_center_y)
        self.platform_now = [self.base_platform]

    def create_start_platform(self):
        count = 0
        for y in range(48,800,Gap_platform):
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
                platform.y -= move/20 
            return move//20
        else:
            return 0
        

    def delete_platform(self):
        count = 0
        for i in range(len(self.platform_now)):
            if self.platform_now[i-count].y <= 0:
                self.platform_now.pop(i-count)
                count += 1
        

    def add_platform(self):
        count = 0
        if self.platform_now[-1].y >= Gap_platform:
            for y in range(int((self.platform_now[-1].y + Gap_platform)//1),SCREEN_HEIGHT,Gap_platform):
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








def check_player_platform_collsion(player_x, player_y, platform_x, platform_y):
    """
    >>> check_player_platform_collsion(60,60,90,24)
    True

    >>> check_player_platform_collsion(100,29,34,23)
    False

    """
    if platform_x - 36 <= player_x <= platform_x + 36 and (platform_y + 9 < player_y - 23 < platform_y + 15):
        return True
    else:

        return False
