"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Rocket"
# Set the and dimensions (width and height)
arcade.open_window(1400, 800, "Rocket")

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Get ready to draw
arcade.start_render()

#Draw de engin
arcade.draw_triangle_filled(700, 100, 800, 700, 600, 700, arcade.color.GRAY)

arcade.draw_triangle_filled(700, 100, 730, 100, 800, 700, arcade.color.GRAY)

arcade.draw_triangle_filled(700, 100, 670, 100, 600, 700, arcade.color.GRAY)

#Draw tiny wings

arcade.draw_lrtb_rectangle_filled(400, 1000, 200, 100, arcade.color.GRAY)









# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

