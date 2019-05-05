import arcade
from newmodels import World



SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
VIEWPORT_MARGIN = 0

route = { 
        "menu":0,
        "game": 1,
        "end":2}



class JumpWINDOW(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
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
            self.start.draw()
        elif self.current_route == route["end"]:
            self.gameover.draw()
            self.restart.draw()
        else:
            self.platform_list.draw()
            self.player.draw()
            score = f"{self.world.score}"
            
            arcade.draw_text(score, 100, 200,
                            arcade.color.BLACK, font_size=14)



    def setup_game(self,width,height):
        self.background = arcade.load_texture("images/background.jpg")
        self.world = World(width, height)
        self.player = ModelSprite(
            'images/character.png', model=self.world.character)
        self.platform_list = Platform_drawer(
            self.world.platform_now.create_start_platform())
        arcade.set_background_color(arcade.color.WHITE)


    def setup_menu(self, width, height):
        SCALE = 0.5
        self.start = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT/2)

        self.start.append_texture(arcade.load_texture("images/start1.png",scale=SCALE))
        self.start.append_texture(arcade.load_texture("images/start2.png",scale=SCALE))
        self.start.set_texture(0)
        self.start.texture_change_frames = 30


    def end_game(self):
        SCALE = 0.25
        self.gameover = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT-150)
        self.gameover.append_texture(arcade.load_texture("images/gameover.png",scale=0.5))
        self.gameover.set_texture(0)
        self.gameover.texture_change_frames = 20

        self.restart = arcade.AnimatedTimeSprite(center_x=SCREEN_WIDTH/2,center_y=SCREEN_HEIGHT/2 - 200)
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
            self.gameover.update()
            self.start.update()
            self.restart.update_animation()


    def on_key_press(self, key, key_modifiers):
        # if not self.world.is_started():
        #     self.world.start()
        if self.current_route == route["menu"]:
            if key == arcade.key.ENTER:
                self.current_route = route["game"]
        elif self.current_route == route["game"]:
            self.world.on_key_press(key, key_modifiers)
        elif self.current_route == route["end"]:
            if key == arcade.key.ENTER:
                self.current_route = route["game"]
                self.setup_game(self.width,self.height)



    def on_key_release(self, key, key_modifiers):
        self.world.on_key_relese(key, key_modifiers)
        

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

    def draw_sprite(self,sprite,x,y):
        sprite.set_position(x,y)
        sprite.draw()


    def draw(self):
        for platform in self.platform_list:
            if platform.name == 1:
                self.draw_sprite(self.platform_sprite,platform.x,platform.y)
            else:
                self.draw_sprite(self.platform_moving_sprite,platform.x,platform.y)
            
            
        



def main():
    window = JumpWINDOW(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == "__main__":
    main()


