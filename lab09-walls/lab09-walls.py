import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Zombie Labyrinth"

MOVEMENT_SPEED = 2
ENEMY_SPEED = 1


class Room:
    def __init__(self):
        self.wall_list = arcade.SpriteList()
        self.background = None


def setup_labyrinth():
    room = Room()

    for y in range(0, SCREEN_HEIGHT, SPRITE_SIZE):
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if x == 0 or y == 0 or x == SCREEN_WIDTH - SPRITE_SIZE or y == SCREEN_HEIGHT - SPRITE_SIZE or (
                    x % (3 * SPRITE_SIZE) == 0 and y % (2 * SPRITE_SIZE) == 0):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
    return room


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.room = None
        self.player_sprite = None
        self.enemy_list = None
        self.victim_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.enemy_physics_engines = []
        self.is_zombie = False

    def setup(self):
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.enemy_list = arcade.SpriteList()
        for i in range(2):
            enemy = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", SPRITE_SCALING)
            enemy.center_x = 300 + i * 200
            enemy.center_y = 300
            self.enemy_list.append(enemy)

        self.victim_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", SPRITE_SCALING)
        self.victim_sprite.center_x = SCREEN_WIDTH - 200
        self.victim_sprite.center_y = SCREEN_HEIGHT - 200

        self.room = setup_labyrinth()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.room.wall_list)
        self.enemy_physics_engines = [arcade.PhysicsEngineSimple(enemy, self.room.wall_list) for enemy in
                                      self.enemy_list]

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.room.background)
        self.room.wall_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        if not self.is_zombie:
            self.victim_sprite.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S):
            self.player_sprite.change_y = 0
        elif key in (arcade.key.A, arcade.key.D):
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
        for engine in self.enemy_physics_engines:
            engine.update()

        for enemy in self.enemy_list:
            if enemy.center_x < self.player_sprite.center_x:
                enemy.change_x = ENEMY_SPEED
            elif enemy.center_x > self.player_sprite.center_x:
                enemy.change_x = -ENEMY_SPEED

            if enemy.center_y < self.player_sprite.center_y:
                enemy.change_y = ENEMY_SPEED
            elif enemy.center_y > self.player_sprite.center_y:
                enemy.change_y = -ENEMY_SPEED

            enemy.update()
            if arcade.check_for_collision(self.player_sprite, enemy):
                self.is_zombie = True
                self.player_sprite.texture = arcade.load_texture(
                    ":resources:images/animated_characters/zombie/zombie_idle.png")

        if self.is_zombie and arcade.check_for_collision(self.player_sprite, self.victim_sprite):
            self.is_zombie = False
            self.player_sprite.texture = arcade.load_texture(
                ":resources:images/animated_characters/female_person/femalePerson_idle.png")
            self.victim_sprite.kill()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
