import arcade
from models import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750


class JumpWINDOW(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("images/background.jpg")
        self.world = World(width,height)
        self.platform = ModelSprite('images/platform1.png',model=self.world.base_platform)
        self.character = ModelSprite('images/character.png',model=self.world.character)


        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
        SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH+50, SCREEN_HEIGHT, self.background)
        self.platform.draw()
        self.character.draw()
    


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




def main():
    window = JumpWINDOW(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == "__main__":
    main()


