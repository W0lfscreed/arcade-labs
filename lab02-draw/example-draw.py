import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Tractor(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Variables para la posición del tractor
        self.tractor_x = 600
        self.tractor_y = 120

        # Inicializar joystick como None
        self.joystick = None

        # Detectar joystick
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()

    def on_draw(self):
        self.clear()

        # Set the background color
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Get ready to draw
        arcade.start_render()

        # Draw the grass
        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

        # --- Draw the barn ---

        # Barn cement base
        arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BISQUE)

        # Bottom half
        arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

        # Left-bottom window
        arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

        # Right-bottom window
        arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

        # Barn door
        arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BLACK_BEAN)

        # Rail above the door
        arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)

        # Draw second level of barn
        arcade.draw_polygon_filled([[20, 350],
                                    [100, 470],
                                    [280, 470],
                                    [360, 340]],
                                   arcade.color.BROWN)

        # Draw loft of barn
        arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

        # Left-top window
        arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)

        # Right-top window
        arcade.draw_rectangle_filled(250, 440, 30, 40, arcade.color.BONE)
        arcade.draw_rectangle_filled(250, 440, 20, 30, arcade.color.BLACK)

        # Draw 2nd level door
        arcade.draw_rectangle_outline(190, 310, 30, 60, arcade.color.BONE, 5)

        # --- Draw the tractor ---

        # Dibujar el motor
        arcade.draw_rectangle_filled(self.tractor_x, self.tractor_y, 140, 70, arcade.color.GRAY)
        arcade.draw_rectangle_filled(self.tractor_x - 10, self.tractor_y - 15, 90, 40, arcade.color.BLACK)

        # Chimenea
        arcade.draw_rectangle_filled(self.tractor_x - 20, self.tractor_y + 55, 10, 40, arcade.color.BLACK)

        # Rueda trasera
        arcade.draw_circle_filled(self.tractor_x - 110, self.tractor_y - 10, 50, arcade.color.BLACK)
        arcade.draw_circle_filled(self.tractor_x - 110, self.tractor_y - 10, 45, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(self.tractor_x - 110, self.tractor_y - 10, 35, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(self.tractor_x - 110, self.tractor_y - 10, 10, arcade.color.RED)

        # Rueda delantera
        arcade.draw_circle_filled(self.tractor_x + 50, self.tractor_y - 30, 30, arcade.color.BLACK)
        arcade.draw_circle_filled(self.tractor_x + 50, self.tractor_y - 30, 25, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(self.tractor_x + 50, self.tractor_y - 30, 18, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(self.tractor_x + 50, self.tractor_y - 30, 5, arcade.color.RED)


    #mover el tractor con el joystiks
    def update(self, delta_time):
        """ Actualiza la posición del tractor con el joystick """
        if self.joystick:
            self.tractor_x += self.joystick.x * 200 * delta_time
            self.tractor_y += self.joystick.y * 200 * delta_time

            self.tractor_x = max(0, min(self.tractor_x, SCREEN_WIDTH))
            self.tractor_y = max(0, min(self.tractor_y, SCREEN_HEIGHT))




def main():
    window = Tractor()
    arcade.run()


main()

#mover el tractor con el ratón
#    def on_mouse_motion(self, x, y, dx, dy):
#        """ Mueve el tractor con el ratón """
#        self.tractor_x = x
#        self.tractor_y = y