import arcade
from newmodels import World


SCREEN_TITLE = "Mage jumping"
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
VIEWPORT_MARGIN = 0

route = { 
        "menu":0,
        "game": 1,
        "end":2}



class JumpWINDOW(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height,SCREEN_TITLE)
        self.all_highscore = 0
        self.current_route = route['menu']
        self.background = arcade.load_texture("images/background.jpg")

        self.setup_menu(self.width, self.height)
        self.setup_game(self.width,self.height)
        self.end_game()



    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH+50, SCREEN_HEIGHT, self.background)
        if self.current_route == route["menu"]:
            self.logo.draw()
            self.start.draw()
            arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,center_y=50,width=200,height=30,texture = arcade.load_texture("images/esctoexit.png"))
            self.platform1.draw()
            self.platform2.draw()
            self.platform3.draw()
            arcade.draw_text("'If you hit you will jump'",230,450,arcade.color.BLACK, font_size=15)
            arcade.draw_text("'If you hit you will jump'\n'Can move'",230,325,arcade.color.BLACK, font_size=15)
            arcade.draw_text("'If you hit you will jump'\n'double hit will disappear'",230,225,arcade.color.BLACK, font_size=15)
            self.button.draw()
            self.move_left.draw()
            self.move_right.draw()
        elif self.current_route == route["end"]:
            if self.all_highscore <= self.world.score:
                self.all_highscore = self.world.score
            self.gameover.draw()
            self.highscore.draw()
            self.draw_score(self.all_highscore,SCREEN_HEIGHT-300)
            self.draw_score(self.world.score,SCREEN_HEIGHT-400)
            self.score.draw()
            self.restart.draw()
            arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,center_y=50,width=200,height=30,texture = arcade.load_texture("images/esctoexit.png"))
        else:
            self.platform_list.draw()
            if self.world.character.left == True:
                self.player.draw()
            else:
                self.player_right.draw()
                
            score = f"score: {self.world.score}"
            
            arcade.draw_text(score, SCREEN_WIDTH-120, SCREEN_HEIGHT-50,
                            arcade.color.BLACK, font_size=20)



    def setup_game(self,width,height):
        self.background = arcade.load_texture("images/background.jpg")
        self.world = World(width, height)
        self.player = ModelSprite(
            "images/character.png", model=self.world.character)
        self.player_right = ModelSprite(
            "images/character_left.png", model=self.world.character)
        
        self.platform_list = Platform_drawer(
            self.world.platform_now.create_start_platform())
        arcade.set_background_color(arcade.color.WHITE)


    def setup_menu(self, width, height):
        SCALE = 0.5
        x_platform = 100
        self.start = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=120)

        self.start.append_texture(arcade.load_texture("images/start1.png",scale=SCALE))
        self.start.append_texture(arcade.load_texture("images/start2.png",scale=SCALE))
        self.start.set_texture(0)
        self.start.texture_change_frames = 20

        self.platform1 = arcade.AnimatedTimeSprite(center_x=x_platform,center_y=450)
        self.platform1.append_texture(arcade.load_texture("images/platform1.png",scale=1))
        self.platform1.set_texture(0)

        self.platform2 = arcade.AnimatedTimeSprite(center_x=x_platform,center_y=350)
        self.platform2.append_texture(arcade.load_texture("images/platform_move.png",scale=1))
        self.platform2.set_texture(0)
        
        self.platform3 = arcade.AnimatedTimeSprite(center_x=x_platform,center_y=250)
        self.platform3.append_texture(arcade.load_texture("images/platform_hit.png",scale=1))
        self.platform3.set_texture(0)

        self.button = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=530)
        self.button.append_texture(arcade.load_texture("images/button.png",scale=0.5))
        self.button.set_texture(0)

        self.move_left = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2-140,center_y=530)
        self.move_left.append_texture(arcade.load_texture("images/moveleft.png",scale=1))
        self.move_left.set_texture(0)

        self.move_right = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2+140,center_y=530)
        self.move_right.append_texture(arcade.load_texture("images/moveright.png",scale=1))
        self.move_right.set_texture(0)

        self.logo = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=670)
        self.logo.append_texture(arcade.load_texture("images/logo.png",scale=0.1))
        self.logo.set_texture(0)


    def end_game(self):
        SCALE = 0.3

        self.gameover = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT-100)
        self.gameover.append_texture(arcade.load_texture("images/gameover.png",scale=0.73))
        self.gameover.set_texture(0)
        self.gameover.texture_change_frames = 20

        self.highscore = arcade.AnimatedTimeSprite(
            center_x=SCREEN_WIDTH/2-100, center_y=SCREEN_HEIGHT-300)
        self.highscore.append_texture(
            arcade.load_texture("images/highscore.png", scale = 0.35))
        self.highscore.set_texture(0)



        self.score = arcade.AnimatedTimeSprite(
            center_x=SCREEN_WIDTH/2-50, center_y=SCREEN_HEIGHT-400)
        self.score.append_texture(
            arcade.load_texture("images/score.png", scale = 0.45))
        self.score.set_texture(0)

        

        self.restart = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT/2 - 250)
        self.restart.append_texture(arcade.load_texture("images/restart.png",scale=SCALE))
        self.restart.append_texture(arcade.load_texture("images/restart1.png",scale=SCALE))
        self.restart.set_texture(0)
        self.restart.texture_change_frames = 30



    def update(self, delta):
        if self.current_route == route["menu"]:
            self.start.update()
            self.start.update_animation()
        elif self.current_route == route["game"]:
            self.world.update(delta)
            if self.world.is_dead():
                self.current_route = route["end"]
        elif self.current_route == route["end"]:
            self.restart.update()
            self.restart.update_animation()


    def on_key_press(self, key, key_modifiers):
        # if not self.world.is_started():
        #     self.world.start()
        if self.current_route == route["menu"]:
            if key == arcade.key.ENTER:
                self.current_route = route["game"]
            elif key == arcade.key.ESCAPE:
                exit()
        elif self.current_route == route["game"]:
            self.world.on_key_press(key, key_modifiers)
        elif self.current_route == route["end"]:
            if key == arcade.key.ENTER:
                self.current_route = route["game"]
                self.setup_game(self.width,self.height)
            elif key == arcade.key.ESCAPE:
                exit()
                

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_relese(key, key_modifiers)
        
    def draw_score(self,score,y):
        gap = 35
        center_x = SCREEN_WIDTH/2 + gap
        for num in str(int(score)):
            arcade.draw_texture_rectangle(center_x= center_x,center_y=y,width=45,height=66,texture = arcade.load_texture(f"images/{num}.png"))
            center_x += gap
    


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class Platform_drawer:
    def __init__(self,platform_list):
        self.platform_list = platform_list
        self.platform_sprite = arcade.Sprite('images/platform1.png')
        self.platform_moving_sprite = arcade.Sprite('images/platform_move.png')
        self.platform_hit_sprite = arcade.Sprite('images/platform_hit.png')


    def draw_sprite(self,sprite,x,y):
        sprite.set_position(x,y)
        sprite.draw()


    def draw(self):
        for platform in self.platform_list:
            if platform.name == 1:
                self.draw_sprite(self.platform_sprite,platform.x,platform.y)
            elif platform.name == 2:
                self.draw_sprite(self.platform_moving_sprite,platform.x,platform.y)
            elif platform.name == 3:
                self.draw_sprite(self.platform_hit_sprite,platform.x,platform.y)




def create_sprite(x,y,name,Scale):
    sprite = arcade.AnimatedTimeSprite(x,y)
    sprite.append_texture(arcade.load_texture(f"images/{name}.png",scale=Scale))
    sprite.set_texture(0)
    return sprite



def main():
    window = JumpWINDOW(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == "__main__":
    main()


