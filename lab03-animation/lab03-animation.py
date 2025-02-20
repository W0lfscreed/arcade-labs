# Import the "arcade" library
import arcade
from arcade import draw_circle_filled

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_fondo():
    arcade.set_background_color(arcade.color.LIGHT_BLUE)

def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, 800, 50, 0, arcade.color.DARK_BROWN)


def circo():
    draw_circle_filled(400,500,17,arcade.color.RED)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw circo")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()


    draw_ground()
    circo()
    arcade.finish_render()
    arcade.run()

main()