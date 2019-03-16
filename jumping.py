import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700


class JumpWINDOW(arcade.Window):
    def __init__(self, width, hight):
        super().__init__(width, hight)
        self.background = arcade.load_texture("images/background.jpg")

        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(
        SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)



def main():
    window = JumpWINDOW(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


if __name__ == "__main__":
    main()
