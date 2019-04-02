import arcade
from models import World


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
VIEWPORT_MARGIN = 0

class JumpWINDOW(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("images/background.jpg")
        self.world = World(width,height)
        self.character = ModelSprite('images/character.png',model=self.world.character)
        self.platform_list = Platform_drawer(self.world.platform_now.create_start_platform())
        self.view_bottom = 375
        self.view_left = 0
        arcade.set_background_color(arcade.color.WHITE)
    
    def setup(self):
        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
        SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH+50, SCREEN_HEIGHT, self.background)
        self.platform_list.draw()
        self.character.draw()

    def update(self, delta):
    
        self.world.update(delta)
        


    def on_key_press(self, key, key_modifiers):
        
        self.world.on_key_press(key, key_modifiers)

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

    def draw_sprite(self,sprite,x,y):
        sprite.set_position(x,y)
        sprite.draw()


    def draw(self):
        for platform in self.platform_list:
            self.draw_sprite(self.platform_sprite,platform.x,platform.y)
            
            
        


def main():
    window = JumpWINDOW(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == "__main__":
    main()


